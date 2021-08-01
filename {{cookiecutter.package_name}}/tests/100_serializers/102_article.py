import datetime

import pytz

from django.conf import settings

from {{ cookiecutter.app_name }}.factories import ArticleFactory, BlogFactory
from {{ cookiecutter.app_name }}.serializers import ArticleSerializer


def test_article_serialize_single(db):
    """
    Single object serialization.
    """
    default_tz = pytz.timezone(settings.TIME_ZONE)

    # Create blog
    foo = BlogFactory(title="Foo")

    # Create article
    lorem = ArticleFactory(
        blog=foo,
        title="Lorem",
        content="Ipsume salace nec vergiture",
        publish_start=default_tz.localize(datetime.datetime(2012, 10, 15, 12, 00)),
    )

    # Serialize article
    serializer = ArticleSerializer(lorem, context={"request": None})

    expected = {
        "id": lorem.id,
        "url": "/api/articles/{}/".format(lorem.id),
        "view_url": "/{}/{}/".format(foo.id, lorem.id),
        "blog": {
            "id": foo.id,
            "url": "/api/blogs/{}/".format(foo.id),
            "view_url": "/{}/".format(foo.id),
            "title": "Foo",
        },
        "title": "Lorem",
        "content": "Ipsume salace nec vergiture",
        "publish_start": "2012-10-15T12:00:00-05:00",
    }

    assert expected == serializer.data


def test_article_serialize_many(db):
    """
    Many objects serialization.
    """
    default_tz = pytz.timezone(settings.TIME_ZONE)

    # Create some blogs
    foo = BlogFactory(title="Foo")
    bar = BlogFactory(title="Bar")

    # Create some articles
    lorem = ArticleFactory(
        blog=foo,
        title="Lorem",
        content="Ipsume salace nec vergiture",
        publish_start=default_tz.localize(datetime.datetime(2012, 10, 15, 12, 00)),
    )
    bonorum = ArticleFactory(
        blog=bar,
        title="Bonorum",
        content="Sed ut perspiciatis unde",
        publish_start=default_tz.localize(datetime.datetime(2021, 8, 7, 15, 30)),
    )

    # Serialize articles
    serializer = ArticleSerializer(
        [lorem, bonorum],
        many=True,
        context={"request": None}
    )

    expected = [
        {
            "id": lorem.id,
            "url": "/api/articles/{}/".format(lorem.id),
            "view_url": "/{}/{}/".format(foo.id, lorem.id),
            "blog": {
                "id": foo.id,
                "url": "/api/blogs/{}/".format(foo.id),
                "view_url": "/{}/".format(foo.id),
                "title": "Foo",
            },
            "title": "Lorem",
            "content": "Ipsume salace nec vergiture",
            "publish_start": "2012-10-15T12:00:00-05:00",
        },
        {
            "id": bonorum.id,
            "url": "/api/articles/{}/".format(bonorum.id),
            "view_url": "/{}/{}/".format(bar.id, bonorum.id),
            "blog": {
                "id": bar.id,
                "url": "/api/blogs/{}/".format(bar.id),
                "view_url": "/{}/".format(bar.id),
                "title": "Bar",
            },
            "title": "Bonorum",
            "content": "Sed ut perspiciatis unde",
            "publish_start": "2021-08-07T15:30:00-05:00",
        },
    ]

    assert expected == serializer.data

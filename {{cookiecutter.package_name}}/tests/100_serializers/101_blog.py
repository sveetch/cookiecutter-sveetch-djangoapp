from {{ cookiecutter.app_name }}.factories import ArticleFactory, BlogFactory
from {{ cookiecutter.app_name }}.serializers import BlogSerializer


def test_blog_serialize_single(db):
    """
    Single object serialization.
    """
    # Create blog
    blog = BlogFactory(title="Foo")

    # Serialize blog
    serializer = BlogSerializer(blog, context={"request": None})

    expected = {
        "id": blog.id,
        "url": "/api/blogs/{}/".format(blog.id),
        "view_url": "/{}/".format(blog.id),
        "title": "Foo",
        "article_count": 0,
    }

    assert expected == serializer.data


def test_blog_serialize_many(db):
    """
    Many objects serialization.
    """
    # Create some blogs
    foo = BlogFactory(title="Foo")
    bar = BlogFactory(title="Bar")

    # Create article
    ArticleFactory(blog=foo, title="Lorem")

    # Serialize blogs
    serializer = BlogSerializer([foo, bar], many=True, context={"request": None})

    expected = [
        {
            "id": foo.id,
            "url": "/api/blogs/{}/".format(foo.id),
            "view_url": "/{}/".format(foo.id),
            "title": "Foo",
            "article_count": 1,
        },
        {
            "id": bar.id,
            "url": "/api/blogs/{}/".format(bar.id),
            "view_url": "/{}/".format(bar.id),
            "title": "Bar",
            "article_count": 0,
        },
    ]

    assert expected == serializer.data

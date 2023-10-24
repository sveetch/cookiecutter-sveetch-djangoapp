from django.core.exceptions import ValidationError

import pytest

from {{ cookiecutter.app_name }}.models import Blog, Article


def test_basic(db, tests_settings):
    """
    Basic model saving with required fields should not fail
    """
    blog = Blog(
        title="Foo",
    )
    blog.save()

    article = Article(
        blog=blog,
        title="Bar",
    )
    article.full_clean()
    article.save()

    url = "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{blog_pk}/{article_pk}/".format(
        blog_pk=blog.id,
        article_pk=article.id,
    )

    assert 1 == Article.objects.filter(title="Bar").count()
    assert "Bar" == article.title
    assert blog == article.blog
    assert url == article.get_absolute_url()


def test_required_fields(db):
    """
    Basic model validation with missing required files should fail
    """
    blog = Blog(
        title="Foo",
    )
    blog.save()

    article = Article()

    with pytest.raises(ValidationError) as excinfo:
        article.full_clean()

    assert excinfo.value.message_dict == {
        "blog": ["This field cannot be null."],
        "title": ["This field cannot be blank."],
    }

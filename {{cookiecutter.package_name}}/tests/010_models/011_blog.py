from django.core.exceptions import ValidationError

import pytest

from {{ cookiecutter.app_name }}.models import Blog


def test_basic(db):
    """
    Basic model validation with required fields should not fail
    """
    blog = Blog(
        title="Foo",
    )
    blog.full_clean()
    blog.save()

    url = "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{blog_pk}/".format(
        blog_pk=blog.id,
    )

    assert 1 == Blog.objects.filter(title="Foo").count()
    assert "Foo" == blog.title
    assert url == blog.get_absolute_url()


def test_required_fields(db):
    """
    Basic model validation with missing required files should fail
    """
    blog = Blog()

    with pytest.raises(ValidationError) as excinfo:
        blog.full_clean()

    assert excinfo.value.message_dict == {
        "title": ["This field cannot be blank."],
    }

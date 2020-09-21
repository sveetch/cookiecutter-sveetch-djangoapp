from django.core.exceptions import ValidationError

import pytest

from {{ cookiecutter.app_name }}.models import Blog


def test_basic(db):
    """
    Basic model validation with required fields should not fail
    """
    instance = Blog(
        title="Foo",
    )
    instance.full_clean()
    instance.save()

    assert 1 == Blog.objects.filter(title="Foo").count()
    assert "Foo" == instance.title


def test_required_fields(db):
    """
    Basic model validation with missing required files should fail
    """
    instance = Blog()

    with pytest.raises(ValidationError) as excinfo:
        instance.full_clean()

    assert excinfo.value.message_dict == {
        "title": ["This field cannot be blank."],
    }

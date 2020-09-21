
from {{ cookiecutter.app_name }}.factories import BlogFactory


def test_creation(db):
    """
    Factory should correctly create a new object without any errors
    """
    instance = BlogFactory(title="foo")
    assert instance.title == "foo"

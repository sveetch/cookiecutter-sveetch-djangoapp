
from {{ cookiecutter.app_name }}.models import Blog


def test_basic(db):
    """
    Basic model saving with required fields should not fail
    """
    instance = Blog(
        title="Foo",
    )
    instance.save()

    assert 1 == Blog.objects.filter(title="Foo").count()
    assert "Foo" == instance.title

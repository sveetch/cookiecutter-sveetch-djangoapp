from {{ cookiecutter.app_name }}.factories import ArticleFactory
from {{ cookiecutter.app_name }}.models import Blog


def test_creation(db):
    """
    Factory should correctly create a new object without any errors
    """
    article = ArticleFactory(title="foo")

    assert article.title == "foo"
    assert isinstance(article.blog, Blog) is True

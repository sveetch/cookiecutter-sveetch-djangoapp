
from {{ cookiecutter.app_name }}.models import Blog, Article


def test_basic(db):
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
    article.save()

    assert 1 == Article.objects.filter(title="Bar").count()
    assert "Bar" == article.title
    assert blog == article.blog

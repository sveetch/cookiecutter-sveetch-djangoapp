from tests.utils import html_element, html_pyquery

from {{ cookiecutter.app_name }}.factories import ArticleFactory, BlogFactory
from {{ cookiecutter.app_name }}.models import Article, Blog


def test_article_detail_404(db, client):
    """
    Try to reach unexisting article should return a 404 response.
    """
    blog1 = BlogFactory(title="blog1")

    url = "/{blog_pk}/1/".format(blog_pk=blog1.id)

    response = client.get(url)

    assert response.status_code == 404


def test_article_detail_noblog(db, client):
    """
    If required blog ID in url does not exists, article detail should return a
    404 response.
    """
    url = "/42/1/"

    response = client.get(url)

    assert response.status_code == 404


def test_article_detail_content(db, client):
    """
    Article content should be displayed correctly.
    """
    blog = BlogFactory(title="blog1")
    article = ArticleFactory(blog=blog)

    url = "/{blog_pk}/{article_pk}/".format(
        blog_pk=blog.id,
        article_pk=article.id,
    )

    response = client.get(url)

    assert response.status_code == 200

    dom = html_pyquery(response)
    blog_title = dom.find(".article-detail p")
    article_title = dom.find(".article-detail h2")
    article_content = dom.find(".article-detail div.content")

    assert blog_title.text() == blog.title
    assert article_title.text() == article.title
    assert article_content.text() == article.content

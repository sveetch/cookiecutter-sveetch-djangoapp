from {{ cookiecutter.app_name }}.utils.tests import html_pyquery

from {{ cookiecutter.app_name }}.factories import ArticleFactory, BlogFactory


def test_article_detail_404(db, client{% if cookiecutter.include_cmsplugin %}, cms_homepage{% endif %}):
    """
    Try to reach unexisting article should return a 404 response.
    """
    blog1 = BlogFactory(title="blog1")

    url = "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{blog_pk}/1/".format(blog_pk=blog1.id)

    response = client.get(url, follow=True)

    assert response.status_code == 404


def test_article_detail_noblog(db, client{% if cookiecutter.include_cmsplugin %}, cms_homepage{% endif %}):
    """
    If required blog ID in url does not exists, article detail should return a
    404 response.
    """
    url = "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}42/1/"

    response = client.get(url, follow=True)

    assert response.status_code == 404


def test_article_detail_content(db, client{% if cookiecutter.include_cmsplugin %}, cms_homepage{% endif %}):
    """
    Article content should be displayed correctly.
    """
    blog = BlogFactory(title="blog1")
    article = ArticleFactory(blog=blog)

    url = "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{blog_pk}/{article_pk}/".format(
        blog_pk=blog.id,
        article_pk=article.id,
    )

    response = client.get(url)

    assert response.status_code == 200

    dom = html_pyquery(response)
    blog_title = dom.find(".article-detail .blog-title")
    article_title = dom.find(".article-detail .title")
    article_content = dom.find(".article-detail .content")

    assert blog_title.text() == blog.title
    assert article_title.text() == article.title
    # Avoid text() method to remove white spaces since content may contain some
    # line breaks
    assert article_content.text(squash_space=False) == article.content

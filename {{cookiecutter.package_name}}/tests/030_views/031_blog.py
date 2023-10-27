from {{ cookiecutter.app_name }}.utils.tests import html_pyquery

from {{ cookiecutter.app_name }}.factories import ArticleFactory, BlogFactory
from {{ cookiecutter.app_name }}.models import Article, Blog


def test_blog_index_empty(db, client{% if cookiecutter.include_cmsplugin|lower == 'true' %}, cms_homepage{% endif %}):
    """
    Without any existing blog, index view should just return the empty text.
    """
    response = client.get("/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}")

    assert response.status_code == 200

    dom = html_pyquery(response)
    content = dom.find(".blog-list li")[0].text

    assert "No blogs yet." == content


def test_blog_index_basic(db, client{% if cookiecutter.include_cmsplugin|lower == 'true' %}, cms_homepage{% endif %}):
    """
    Blog index view should list every blog.
    """
    blog1 = BlogFactory(title="blog1")
    blog2 = BlogFactory(title="blog2")

    response = client.get("/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}")

    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".blog-list li")

    expected_titles = [
        "blog1",
        "blog2",
    ]

    expected_urls = [
        "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{blog_pk}/".format(blog_pk=blog1.id),
        "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{blog_pk}/".format(blog_pk=blog2.id),
    ]

    assert expected_titles == [item.find("a").text for item in items]

    assert expected_urls == [item.find("a").get("href") for item in items]


def test_blog_index_pagination(settings, db, client{% if cookiecutter.include_cmsplugin|lower == 'true' %}, cms_homepage{% endif %}):
    """
    Blog index view is paginated from setting limit, not every blog is listed
    on the same page.
    """
    # Twice the blog pagination limit plus one entry so we can expect three
    # result pages
    blog_total = (settings.BLOG_PAGINATION * 2) + 1

    BlogFactory.create_batch(blog_total)

    assert blog_total == Blog.objects.all().count()

    # First result page
    response = client.get("/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}")
    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".blog-list li")
    assert settings.BLOG_PAGINATION == len(items)
    # Check pagination is correct
    pages = dom.find(".pagination a")
    assert 3 == len(pages)

    # Second result page
    response = client.get("/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}?page=2")
    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".blog-list li")
    assert settings.BLOG_PAGINATION == len(items)
    # Check current page is correct
    active = dom.find(".pagination a.active")
    assert 1 == len(active)
    assert "2" == active.text()

    # Third result page
    response = client.get("/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}?page=3")

    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".blog-list li")
    assert 1 == len(items)


def test_blog_detail_404(db, client{% if cookiecutter.include_cmsplugin|lower == 'true' %}, cms_homepage{% endif %}):
    """
    Try to reach unexisting blog should return a 404 response.
    """
    url = "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}42/"

    response = client.get(url, follow=True)

    assert response.status_code == 404


def test_blog_detail_no_article(db, client{% if cookiecutter.include_cmsplugin|lower == 'true' %}, cms_homepage{% endif %}):
    """
    Without any related article, blog detail view should just contains its
    content and return the empty text for article list.
    """
    blog1 = BlogFactory(title="blog1")

    url = "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{blog_pk}/".format(blog_pk=blog1.id)

    response = client.get(url)

    assert response.status_code == 200

    dom = html_pyquery(response)

    blog_title = dom.find(".blog-detail h2")
    assert blog_title.text() == blog1.title

    content = dom.find(".article-list li")[0].text
    assert "No articles yet." == content


def test_blog_detail_article_pagination(settings, db, client{% if cookiecutter.include_cmsplugin|lower == 'true' %}, cms_homepage{% endif %}):
    """
    Blog index detail has a paginated list of article and so not every blog
    articles are listed on the same page.
    """
    blog1 = BlogFactory(title="blog1")

    blog_url = "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{blog_pk}/".format(blog_pk=blog1.id)

    article_total = (settings.ARTICLE_PAGINATION * 2) + 1

    ArticleFactory.create_batch(article_total, blog=blog1)

    assert article_total == Article.objects.all().count()

    # First result page
    response = client.get(blog_url)
    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".article-list li")
    assert settings.ARTICLE_PAGINATION == len(items)
    # Check pagination is correct
    pages = dom.find(".pagination a")
    assert 3 == len(pages)

    # Second result page
    response = client.get(blog_url + "?page=2")
    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".article-list li")
    assert settings.ARTICLE_PAGINATION == len(items)
    # Check current page is correct
    active = dom.find(".pagination a.active")
    assert 1 == len(active)
    assert "2" == active.text()

    # Third result page
    response = client.get(blog_url + "?page=3")

    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".article-list li")
    assert 1 == len(items)

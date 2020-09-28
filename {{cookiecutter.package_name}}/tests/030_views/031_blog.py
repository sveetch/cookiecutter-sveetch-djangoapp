from tests.utils import html_element, html_pyquery

from {{ cookiecutter.app_name }}.factories import BlogFactory
from {{ cookiecutter.app_name }}.models import Blog


def test_blog_index_empty(db, client):
    """
    Without any existing blog, index view should just return the empty text.
    """
    response = client.get("/")

    assert response.status_code == 200

    dom = html_pyquery(response)
    content = dom.find("li")[0].text

    assert "No blogs yet." == content


def test_blog_index_basic(db, client):
    """
    Blog index view should list every blog.
    """
    blog1 = BlogFactory(title="blog1")
    blog2 = BlogFactory(title="blog2")

    response = client.get("/")

    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".blog-list li")

    expected_titles = [
        "blog1",
        "blog2",
    ]

    expected_urls = [
        "/{blog_pk}/".format(blog_pk=blog1.id),
        "/{blog_pk}/".format(blog_pk=blog2.id),
    ]

    assert expected_titles == [item.find("a").text for item in items]

    assert expected_urls == [item.find("a").get("href") for item in items]


def test_blog_index_pagination(settings, db, client):
    """
    Blog index view is paginated from setting limit, not every blog is listed
    on the same page.
    """
    # Twice the blog pagination limit plus one entry so we can expect three
    # result pages
    blog_total = (settings.BLOG_PAGINATION * 2) + 1

    blogs = BlogFactory.create_batch(blog_total)

    assert blog_total == Blog.objects.all().count()

    # First result page
    response = client.get("/")
    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".blog-list li")
    assert settings.BLOG_PAGINATION == len(items)
    # Check pagination is correct
    pages = dom.find(".pagination a")
    assert 3 == len(pages)

    # Second result page
    response = client.get("/?page=2")
    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".blog-list li")
    assert settings.BLOG_PAGINATION == len(items)
    # Check current page is correct
    active = dom.find(".pagination a.active")
    assert 1 == len(active)
    assert "2" == active.text()

    # Third result page
    response = client.get("/?page=3")

    assert response.status_code == 200

    dom = html_pyquery(response)
    items = dom.find(".blog-list li")
    assert 1 == len(items)

from tests.utils import html_element, html_pyquery

from {{ cookiecutter.app_name }}.factories import BlogFactory


def test_blog_index_empty(db, client):
    """
    Without any existing blog, index view should just return the empty text.
    """
    response = client.get("/")

    assert response.status_code == 200

    dom = html_pyquery(response)

    assert "No blogs yet." == dom.find("li").text()

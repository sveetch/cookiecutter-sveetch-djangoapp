from {{ cookiecutter.app_name }}.factories import BlogFactory


def test_blog_index(db, client):
    """
    Blog index view should list every blog
    """
    response = client.get("/")

    assert response.status_code == 200

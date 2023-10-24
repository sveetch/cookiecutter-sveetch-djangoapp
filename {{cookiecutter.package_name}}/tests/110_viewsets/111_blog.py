import pytest

from rest_framework.test import APIClient

from {{ cookiecutter.app_name }}.factories import BlogFactory, UserFactory
from {{ cookiecutter.app_name }}.models import Blog

from tests.utils import DRF_DUMMY_HOST_URL as HOSTURL


def test_blog_viewset_list(db):
    """
    Read response from API viewset list.
    """
    # Create some blogs
    foo = BlogFactory(title="Foo")
    bar = BlogFactory(title="Bar")

    # Use test client to get blog list
    client = APIClient()
    response = client.get("/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/", format="json")
    json_data = response.json()

    # Expected payload from JSON response
    expected = [
        {
            "id": bar.id,
            "url": "{}/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/{}/".format(
                HOSTURL,
                bar.id
            ),
            "view_url": "{}/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{}/".format(
                HOSTURL,
                bar.id
            ),
            "title": "Bar",
            "article_count": 0,
        },
        {
            "id": foo.id,
            "url": "{}/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/{}/".format(
                HOSTURL,
                foo.id
            ),
            "view_url": "{}/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{}/".format(
                HOSTURL,
                foo.id
            ),
            "title": "Foo",
            "article_count": 0,
        },
    ]

    assert response.status_code == 200
    assert expected == json_data


def test_blog_viewset_detail(db):
    """
    Read response from API viewset detail.
    """
    # Create blog object
    foo = BlogFactory(title="Foo")

    # Use test client to get blog object
    client = APIClient()
    response = client.get(
        "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/{}/".format(foo.id),
        format="json"
    )
    json_data = response.json()

    # Expected payload from JSON response
    expected = {
        "id": foo.id,
        "url": "{}/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/{}/".format(
            HOSTURL,
            foo.id
        ),
        "view_url": "{}/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}{}/".format(
            HOSTURL,
            foo.id
        ),
        "title": "Foo",
        "article_count": 0,
    }

    assert response.status_code == 200
    assert expected == json_data


def test_blog_viewset_forbidden(db):
    """
    Write methods require to be authenticated with the right permissions.
    """
    # Use test client with anonymous user
    client = APIClient()

    # Create blog object
    foo = BlogFactory(title="Foo")

    # Try to create a new blog
    response = client.post(
        "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/",
        {
            "title": "Ping",
        },
        format="json"
    )
    assert response.status_code == 403

    # Try to edit an existing blog
    response = client.post(
        "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/{}/".format(foo.id),
        {
            "title": "Bar",
        },
        format="json"
    )
    assert response.status_code == 403

    # Try to delete an existing blog
    response = client.delete(
        "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/{}/".format(foo.id),
        format="json"
    )
    assert response.status_code == 403


def test_blog_viewset_post(db):
    """
    Create a new blog with HTTP POST method.
    """
    # Create a superuser to not bother with permissions
    user = UserFactory(flag_is_superuser=True)

    # Use test client with authenticated user to create a new blog
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post(
        "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/",
        {
            "title": "Foo",
        },
        format="json"
    )
    json_data = response.json()

    # Check response status code according to HTTP method
    assert response.status_code == 201

    # Check created object
    blog = Blog.objects.get(pk=json_data["id"])
    assert blog.title == json_data["title"]


def test_blog_viewset_put(db):
    """
    Edit an existing blog with HTTP PUT method.
    """
    # Create a superuser to not bother with permissions
    user = UserFactory(flag_is_superuser=True)

    # Create blog object
    foo = BlogFactory(title="Foo")

    # Use test client with authenticated user to create a new blog
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.put(
        "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/{}/".format(foo.id),
        {
            "title": "Bar",
        },
        format="json"
    )
    json_data = response.json()

    # Check response status code according to HTTP method
    assert response.status_code == 200

    # Check edited object
    blog = Blog.objects.get(pk=foo.id)
    assert blog.title == json_data["title"]


def test_blog_viewset_patch(db):
    """
    Edit an existing blog with HTTP PATCH method.
    """
    # Create a superuser to not bother with permissions
    user = UserFactory(flag_is_superuser=True)

    # Create blog object
    foo = BlogFactory(title="Foo")

    # Use test client with authenticated user to create a new blog
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.patch(
        "/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/{}/".format(foo.id),
        {
            "title": "Bar",
        },
        format="json"
    )
    json_data = response.json()

    # Check response status code according to HTTP method
    assert response.status_code == 200

    # Check edited object
    blog = Blog.objects.get(pk=foo.id)
    assert blog.title == json_data["title"]


def test_blog_viewset_delete(db):
    """
    Edit an existing blog with HTTP DELETE method.
    """
    # Create a superuser to not bother with permissions
    user = UserFactory(flag_is_superuser=True)

    # Create blog object
    foo = BlogFactory()

    # Use test client with authenticated user to create a new blog
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.delete("/{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}/{% endif %}api/blogs/{}/".format(foo.id))

    # Check response status code according to HTTP method
    assert response.status_code == 204

    # Check deleted object does not exist anymore
    with pytest.raises(Blog.DoesNotExist):
        Blog.objects.get(pk=foo.id)

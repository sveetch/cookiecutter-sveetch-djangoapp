from cms.api import add_plugin

from {{ cookiecutter.app_name }}.cms_plugins import BlogPlugin
from {{ cookiecutter.app_name }}.utils.cms_api import CmsAPI
from {{ cookiecutter.app_name }}.factories import (
    ArticleFactory, BlogFactory, BlogPluginModelFactory, UserFactory
)

from {{ cookiecutter.app_name }}.utils.tests import html_pyquery


def test_form_view_add(db, client, settings):
    """
    Plugin creation form should return a success status code and every
    expected field should be present in HTML.
    """
    user = UserFactory(is_staff=True, is_superuser=True)
    client.force_login(user)
    cmsapi = CmsAPI(author=user)

    # Create a draft page since where we can work
    page, page_content, version = cmsapi.create_page(
        "Dummy",
        template=settings.TEST_PAGE_TEMPLATE,
    )

    # Get placeholder
    placeholder = cmsapi.get_placeholder()

    response = cmsapi.request_plugin_add(client, "BlogPlugin", placeholder.pk)

    # Expected http success status
    assert response.status_code == 200

    # Parse resulting plugin fields
    dom = html_pyquery(response)

    limit_field = dom.find("input#id_limit")
    assert len(limit_field) == 1

    blog_field = dom.find("select#id_blog")
    assert len(blog_field) == 1


def test_form_view_edit(db, client, settings):
    """
    Plugin edition form should return a success status code and every
    expected field should be present in HTML.
    """
    user = UserFactory(is_staff=True, is_superuser=True)
    client.force_login(user)
    cmsapi = CmsAPI(author=user)

    blog = BlogFactory(title="News")
    pluginmodel = BlogPluginModelFactory(blog=blog)

    # Create a draft page since where we can work
    page, page_content, version = cmsapi.create_page(
        "Dummy",
        template=settings.TEST_PAGE_TEMPLATE,
    )

    # Add blog plugin into placeholder
    placeholder = cmsapi.get_placeholder()
    pluginmodel_instance = add_plugin(
        placeholder,
        BlogPlugin,
        "en",
        blog=pluginmodel.blog,
        limit=pluginmodel.limit,
    )

    # Get the edition plugin form url and open it
    response = cmsapi.request_plugin_edit(client, pluginmodel_instance.id)

    # Expected http success status
    assert response.status_code == 200

    # Parse resulting plugin fields
    dom = html_pyquery(response)

    limit_field = dom.find("input#id_limit")
    assert len(limit_field) == 1

    blog_field = dom.find("select#id_blog")
    assert len(blog_field) == 1


def test_render_in_page(db, client, settings):
    """
    Plugin should be properly rendered in a Page depending its options.
    """
    settings.LANGUAGE_CODE = "en"

    user = UserFactory(is_staff=True, is_superuser=True)
    cmsapi = CmsAPI(author=user)

    blog = BlogFactory(title="News")
    ArticleFactory.create_batch(5, blog=blog)
    pluginmodel = BlogPluginModelFactory(blog=blog, limit=3)

    page, page_content, version = cmsapi.create_page(
        "Dummy",
        template=settings.TEST_PAGE_TEMPLATE,
        publish=True,
    )

    # Here we need to give page to get its existing placeholder for content
    placeholder = cmsapi.get_placeholder(page=page)
    # Add blog plugin to placeholder with a limit of articles
    pluginmodel_instance = add_plugin(
        placeholder,
        BlogPlugin,
        settings.LANGUAGE_CODE,
        blog=pluginmodel.blog,
        limit=pluginmodel.limit,
    )
    url = page.get_absolute_url(language=settings.LANGUAGE_CODE)
    response = client.get(url)

    # With limit set, article list should be limited
    dom = html_pyquery(response)
    plugin_container = dom.find(".blog-plugin")
    assert len(plugin_container) == 1
    article_items = dom.find(".blog-plugin .plugin-articles li:not(.empty)")
    assert len(article_items) == 3

    # Change plugin to set not limit
    pluginmodel_instance.limit = 0
    pluginmodel_instance.save()
    url = page.get_absolute_url(language=settings.LANGUAGE_CODE)
    response = client.get(url)

    # With unlimited article list, all blog articles should be displayed
    dom = html_pyquery(response)
    article_items = dom.find(".blog-plugin .plugin-articles li:not(.empty)")
    assert len(article_items) == 5

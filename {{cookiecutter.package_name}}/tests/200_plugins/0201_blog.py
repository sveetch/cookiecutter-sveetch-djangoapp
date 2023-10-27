from cms.api import create_page, add_plugin
from cms.utils.urlutils import admin_reverse

from {{ cookiecutter.app_name }}.cms_plugins import BlogPlugin
from {{ cookiecutter.app_name }}.factories import (
    ArticleFactory, BlogFactory, BlogPluginModelFactory, UserFactory
)

from {{ cookiecutter.app_name }}.utils.tests import html_pyquery


def test_form_view_add(db, client, settings):
    """
    Plugin creation form should return a success status code and every
    expected field should be present in HTML.
    """
    client.force_login(
        UserFactory(is_staff=True, is_superuser=True)
    )

    # Create dummy page
    page = create_page(
        language="en",
        title="Dummy",
        slug="dummy",
        template=settings.TEST_PAGE_TEMPLATES,
    )

    # Get placeholder
    placeholder = page.placeholders.get(slot="content")

    # Get the edition plugin form url and open it
    url = admin_reverse('cms_page_add_plugin')
    response = client.get(url, {
        'plugin_type': 'BlogPlugin',
        'placeholder_id': placeholder.pk,
        'target_language': 'en',
        'plugin_language': 'en',
    })
    # print()
    # print(response.content.decode())
    # print()

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
    client.force_login(
        UserFactory(is_staff=True, is_superuser=True)
    )

    blog = BlogFactory(title="News")
    pluginmodel = BlogPluginModelFactory(blog=blog)

    # Create dummy page
    page = create_page(
        language="en",
        title="Dummy",
        slug="dummy",
        template=settings.TEST_PAGE_TEMPLATES,
    )

    # Add blog plugin to placeholder
    placeholder = page.placeholders.get(slot="content")
    pluginmodel_instance = add_plugin(
        placeholder,
        BlogPlugin,
        "en",
        blog=pluginmodel.blog,
        limit=pluginmodel.limit,
    )

    # Get the edition plugin form url and open it
    url = admin_reverse('cms_page_edit_plugin', args=[pluginmodel_instance.id])
    response = client.get(url)

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

    blog = BlogFactory(title="News")
    ArticleFactory.create_batch(5, blog=blog)
    pluginmodel = BlogPluginModelFactory(blog=blog, limit=3)

    # Create dummy page
    page = create_page(
        language=settings.LANGUAGE_CODE,
        title="Dummy",
        slug="dummy",
        template=settings.TEST_PAGE_TEMPLATES,
    )

    # Add blog plugin to placeholder with a limit of articles
    placeholder = page.placeholders.get(slot="content")
    pluginmodel_instance = add_plugin(
        placeholder,
        BlogPlugin,
        settings.LANGUAGE_CODE,
        blog=pluginmodel.blog,
        limit=pluginmodel.limit,
    )
    page.publish(settings.LANGUAGE_CODE)
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
    page.publish(settings.LANGUAGE_CODE)
    url = page.get_absolute_url(language=settings.LANGUAGE_CODE)
    response = client.get(url)

    # With unlimited article list, all blog articles should be displayed
    dom = html_pyquery(response)
    article_items = dom.find(".blog-plugin .plugin-articles li:not(.empty)")
    assert len(article_items) == 5

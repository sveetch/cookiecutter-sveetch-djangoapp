from django.conf import settings

from cms.utils.urlutils import admin_reverse
from cms.models import Placeholder

try:
    from djangocms_versioning.models import Version
    from djangocms_versioning.constants import DRAFT
    from djangocms_versioning.constants import PUBLISHED
except ImportError:
    Version = None
    DRAFT = None
    PUBLISHED = None


def create_page_helper(title, template=None, language=None, is_home=False,
                       publish=False, **kwargs):
    """
    Helper to quickly create a CMS page.

    Opposed to the legacy ``create_page()`` this helper involves versionning and
    publication.

    Since DjangoCMS 4 has hardly leveled up the way to programmatically create a page
    and publish it, we need some helper around their programmatic API (sigh).

    .. Warning::
        Although the argument ``created_by`` is optionnal, it should always be given
        else you will have trouble to get the page.

    Arguments:
        title (string): Page content title, the page slug will be automatically built
            from this title.
        **kwargs: Any keyword arguments allowed in ``cms.api.create_page``, the most
            noticable ones are: ``created_by``, ``slug``, ``reverse_id``, ``parent``,
            ``in_navigation``, ``soft_root`` and ``login_required``.

    Keyword Arguments:
        template (string): Page content template, if not given the first one from
            setting ``CMS_TEMPLATES`` is used.
        language (string): Language code, if not given the default project language is
            used.
        is_home (boolean): Define page as the new homepage.
        publish (boolean): Define if page should be published with
            'djangocms_versioning' if it is installed. Without versionning there is no
            concept of draft, once saved the page is published so this arg will be
            ignored.

    Returns:
        tuple: This method return a tuple containing respectively the Page object, its
        PageContent object and then its last version object.
    """
    # NOTE: It is recommended to import the API inside function to avoid possible
    # circular imports
    from cms.api import create_page

    page = create_page(
        title,
        template or settings.CMS_TEMPLATES[0][0],
        language or settings.LANGUAGE_CODE,
        **kwargs
    )

    if is_home:
        page.set_as_homepage()

    page_content = page.pagecontent_set(
        manager="admin_manager"
    ).latest_content().last()

    # Force version publish only if 'djangocms_versioning' is available
    if Version:
        version = Version.objects.get(object_id=page_content.id)

        if publish:
            version.publish(kwargs.get("created_by", None))
    else:
        version = None

    return page, page_content, version


class CmsAPI:
    """
    Programmatic API interface for common operations with DjangoCMS.

    This abstract may be suitable to mix within a Unittest class but you will have to
    set attributes ``_author`` and ``_language`` yourself before using methods.

    Attributes:
        _author (User object): User object to use with operation methods that need it.
        _language (string): Language code to use with operation method that need it.
            When undefined it will use the default language from settings.

    Arguments:
        author (User object): User object to use with operation methods that need it.
        language (string): Language code to use with operation method that need it.
            When undefined it will use the default language from settings.
    """
    _CMS_PLUGIN_ADD_URL_PATTERN = "cms_placeholder_add_plugin"
    _CMS_PLUGIN_EDIT_URL_PATTERN = "cms_placeholder_edit_plugin"
    _CMS_DEFAULT_SLOT = "content"

    def __init__(self, *args, **kwargs):
        self._author = kwargs.pop("author", None)
        self._language = kwargs.pop("language", None)

    def get_author(self):
        """
        Wrapper to get defined author from CmsAPI attribute.

        All code needing to use author should use this method so it will raise an error
        without making 'author' argument required.
        """
        if not getattr(self, "_author"):
            raise ValueError(
                "CMS API interface used a method requiring an author but it was not"
                "set. You should set it before."
            )
        return self._author

    def get_language(self, language=None):
        return language or getattr(self, "_language") or settings.LANGUAGE_CODE

    def get_plugin_add_url(self):
        """
        Return the URL to add a new plugin.

        Returns:
            string: The URL.
        """
        return admin_reverse(self._CMS_PLUGIN_ADD_URL_PATTERN)

    def request_plugin_add(self, client, plugin, placeholder, position=None):
        """
        Use a request client to get a plugin creation form.

        .. Note::
            Plugin creation requires more arguments that the edition one because it
            needs to know what kind of plugin and how to create it, opposed to edition
            that just retrieves this from the plugin instance.

        Returns:
            string: The URL.
        """
        url = self.get_plugin_add_url()
        language = self.get_language()

        data = {
            "plugin_type": plugin,
            "placeholder_id": placeholder,
            "cms_path": "/{}/".format(language),
            "plugin_language": language,
            "plugin_position": position or 1,
        }

        return client.get(url, data)

    def get_plugin_edit_url(self, pk=None):
        """
        Return the URL to edit a plugin.

        Keyword Arguments:
            pk (integer or string): The plugin id. If not given it will be replaced by
                a string placeholder ``{}``. This can be useful to reuse the same blank
                pattern multiple times without repeatedly calling this method.

        Returns:
            string: The URL.
        """
        return admin_reverse(self._CMS_PLUGIN_EDIT_URL_PATTERN, args=[pk or "{}"])

    def request_plugin_edit(self, client, pk):
        """
        Use a request client to get a plugin edition form.

        Returns:
            string: The URL.
        """
        url = self.get_plugin_edit_url(pk=pk)

        return client.get(url)

    def _get_versionning(self, grouper, version_state, language=None):
        """
        Get version object of a grouper in a specific state and for a possible language.

        Returns:
            object: Either the Version object if 'djangocms_versioning' is installed or
            None if 'djangocms_versioning' is not available.
        """
        if Version is None:
            return None

        versions = Version.objects.filter_by_grouper(grouper).filter(
            state=version_state
        )
        for version in versions:
            if (
                hasattr(version.content, "language")
                and version.content.language == self.get_language(language)
            ):
                return version

    def publish(self, grouper, language=None):
        """
        Force publishing of a version grouper with 'djangocms_versioning'.
        """
        if Version:
            version = self._get_versionning(grouper, DRAFT, language)
            if version is not None:
                version.publish(self.get_author())

    def unpublish(self, grouper, language=None):
        """
        Force unpublishing of a version grouper with 'djangocms_versioning'.
        """
        if Version:
            version = self._get_versionning(grouper, PUBLISHED, language)
            if version is not None:
                version.unpublish(self.get_author())

    def create_page(self, title, **kwargs):
        """
        Wrap ``create_page_helper`` to enforce default language and author.

        Keyword arguments:
            language (string): Language code to use, default to the default project
                language.
            created_by (User): User object to use instead of the default one (as given
                from CmsAPI init).
        """
        kwargs.setdefault("language", self.get_language())

        author = self.get_author()
        if author and not kwargs.get("created_by"):
            kwargs["created_by"] = author

        return create_page_helper(title, **kwargs)

    def get_placeholder(self, slot=None, page=None):
        """
        Returns:
            object: A queryset of placeholders from a page if page is given else a
            single placeholder (created on the fly with slot name ``content``).
        """
        slot = slot or self._CMS_DEFAULT_SLOT

        if not page:
            return Placeholder.objects.create(slot=slot)
        else:
            return page.get_placeholders(self.get_language()).get(slot=slot)

    def legacy_get_placeholders(self, language):
        from cms.models import PageContent, Placeholder

        page_content = PageContent.objects.get(language=language, page=self)
        return Placeholder.objects.get_for_obj(page_content)

from django.conf import settings
from django.utils.text import slugify

import factory

from cms import models as cms_models
from cms.utils import get_current_site

from .user import UserFactory


class TitleFactory(factory.django.DjangoModelFactory):
    """
    Create random title objects for CMS pages.
    """

    language = settings.LANGUAGE_CODE
    page = None
    title = factory.Faker("catch_phrase")
    path = factory.LazyAttribute(lambda o: o.page.get_path_for_slug(o.slug, o.language))
    slug = factory.LazyAttribute(lambda o: slugify(o.title))

    class Meta:
        model = cms_models.Title
        skip_postgeneration_save = True

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        """
        Update the related page's languages (taken from DjangoCMS's create_page helper).
        """
        super()._after_postgeneration(instance, create, results=results)
        page = instance.page
        if page:
            page_languages = page.get_languages()
            if instance.language not in page_languages:
                page.update_languages(page_languages + [instance.language])


class PageFactory(factory.django.DjangoModelFactory):
    """
    Create random CMS pages.
    """

    changed_by = factory.LazyAttribute(lambda o: slugify(o.user.username))
    created_by = factory.LazyAttribute(lambda o: slugify(o.user.username))
    title = factory.RelatedFactory(TitleFactory, "page")

    # Utility fields
    in_navigation = True
    login_required = False
    parent = None
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = cms_models.Page
        exclude = ["parent", "user"]
        skip_postgeneration_save = True

    @factory.lazy_attribute
    def node(self):
        """
        Create a node for the page (under its parent if applicable).
        """
        site = get_current_site()
        new_node = cms_models.TreeNode(site=site)

        if self.parent:
            return self.parent.node.add_child(instance=new_node)
        return cms_models.TreeNode.add_root(instance=new_node)

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        """
        This hook method is called last when generating an instance from a factory. The
        super method saves the instance one last time after all the "post_generation"
        hooks have played.

        This is the moment to finally publish the pages. If we published the pages
        before this final "save", they would be set back to a pending state and would
        not be in a clean published state.
        """
        super()._after_postgeneration(instance, create, results=results)
        instance.rescan_placeholders()

        if results.get("should_publish", False):
            for language in instance.get_languages():
                instance.publish(language)
            instance.get_public_object().rescan_placeholders()

        instance.refresh_from_db()

    @factory.post_generation
    def should_publish(obj, create, extracted, **kwargs):
        """
        Mark the page for publishing. The actual publishing is done by the
        "_after_post_generation" hook method above.
        """
        if create and extracted:
            return True
        return False

    @factory.post_generation
    def set_homepage(obj, create, extracted, **kwargs):
        """
        Define page as a homepage.
        """
        if create and extracted:
            obj.set_as_homepage()
            return True
        return False

    @factory.post_generation
    def reverse_id(obj, create, extracted, **kwargs):
        """
        Define the page 'reverse_id' attribute.

        This is only for a create strategy.

        If extracted is True, this will copy the Page title slug, be careful that a
        slug is not unique among pages, so it is not safe.

        Else if extracted is not empty its value will be used to fill the attribute,
        obviously the value must be a String.
        """
        if create:
            if extracted is True:
                obj.reverse_id = obj.get_slug()
            elif extracted:
                obj.reverse_id = extracted
        return None

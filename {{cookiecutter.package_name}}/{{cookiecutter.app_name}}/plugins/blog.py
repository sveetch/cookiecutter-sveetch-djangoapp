from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase

from ..forms import BlogPluginForm
from ..models import BlogPluginModel


class BlogPlugin(CMSPluginBase):
    """
    Blog plugin select a blog to list its X last articles.
    """
    module = _("{{ cookiecutter.package_name }}")
    name = _("Blog last articles")
    model = BlogPluginModel
    form = BlogPluginForm
    render_template = "{{ cookiecutter.app_name }}/blog_plugin.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)

        # Limit article queryset if there is any limit upper to zero
        articles = instance.blog.article_set.all().order_by("-publish_start", "title")
        if instance.limit:
            articles = articles[0:instance.limit]

        context.update({
            "instance": instance,
            "articles": articles,
        })

        return context

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse{% if cookiecutter.include_cmsplugin %}

from cms.models.pluginmodel import CMSPlugin{% endif %}


class Blog(models.Model):
    """
    A very simple blog to contain articles.
    """
    title = models.CharField(
        _("title"),
        blank=False,
        max_length=55,
        default="",
        unique=True,
    )
    """
    Required unique title string.
    """

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = [
            "title",
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Return absolute URL to the blog detail view.

        Returns:
            string: An URL.
        """
        return reverse("{{ cookiecutter.app_name }}:blog-detail", args=[
            str(self.id)
        ])
{% if cookiecutter.include_cmsplugin %}

class BlogPluginModel(CMSPlugin):
    """
    Blog plugin model.
    """
    blog = models.ForeignKey(
        Blog,
        related_name="blog_plugin",
        on_delete=models.CASCADE
    )
    """
    Related blog.
    """

    limit = models.IntegerField(
        _("Article limit"),
        blank=False,
        default=0,
        help_text=_("Using 0 as limit means no limit.")
    )
    """
    Maximum number of articles to list from a blog.
    """

    def __str__(self):
        return self.blog.title

    class Meta:
        verbose_name = _("Blog plugin")
        verbose_name_plural = _("Blogs plugins")
{% endif %}
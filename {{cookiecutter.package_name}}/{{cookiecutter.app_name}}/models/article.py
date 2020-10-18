"""
=======
Article
=======

"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from .blog import Blog


class Article(models.Model):
    """
    A simple article for a blog.
    """
    blog = models.ForeignKey(
        Blog,
        verbose_name="Related blog",
        on_delete=models.CASCADE
    )
    """
    Required related blog object.
    """

    title = models.CharField(
        _("title"),
        blank=False,
        max_length=150,
        default="",
    )
    """
    Required title string.
    """

    content = models.TextField(
        _("content"),
        blank=True,
        default="",
    )
    """
    Optionnal text content.
    """

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Return absolute URL to the article detail view.

        Returns:
            string: An URL.
        """
        return reverse("{{ cookiecutter.app_name }}:article-detail", args=[
            str(self.blog.id),
            str(self.id)
        ])

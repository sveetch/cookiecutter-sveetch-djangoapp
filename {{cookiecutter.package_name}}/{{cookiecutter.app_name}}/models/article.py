from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from .blog import Blog


class Article(models.Model):
    """
    Article model.
    """
    blog = models.ForeignKey(
        Blog,
        verbose_name="Related blog",
        on_delete=models.CASCADE
    )
    title = models.CharField(
        _("title"),
        blank=False,
        max_length=150,
        default="",
    )
    content = models.TextField(
        _("content"),
        blank=True,
        default="",
    )

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("{{ cookiecutter.app_name }}:article-detail", args=[
            str(self.blog.id),
            str(self.id)
        ])

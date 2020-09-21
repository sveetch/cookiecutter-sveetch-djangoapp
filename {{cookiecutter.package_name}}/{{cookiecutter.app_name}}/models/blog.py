from django.db import models
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    """
    Blog model.
    """
    title = models.CharField(
        _("title"),
        blank=False,
        max_length=55,
        default="",
        unique=True,
    )

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("{{ cookiecutter.app_name }}:blog-detail", args=[
            str(self.id)
        ])

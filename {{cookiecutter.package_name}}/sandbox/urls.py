"""
URL Configuration for sandbox
"""
from django.conf import settings{% if cookiecutter.include_cmsplugin|lower == 'true' %}
from django.conf.urls.i18n import i18n_patterns{% endif %}
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),{% if cookiecutter.include_api|lower == 'true' %}
    path("api-auth/", include("rest_framework.urls")),{% endif %}{% if cookiecutter.include_cmsplugin|lower == 'true' %}
    path("{{ cookiecutter.app_name }}/", include("{{ cookiecutter.app_name }}.urls")),
    {% else %}
    path("", include("{{ cookiecutter.app_name }}.urls")),
    {% endif %}
]{% if cookiecutter.include_cmsplugin|lower == 'true' %} + i18n_patterns(
    path("", include("cms.urls")),
){% endif %}

# This is only needed when using runserver with settings "DEBUG" enabled
if settings.DEBUG:
    urlpatterns = (
        urlpatterns
        + staticfiles_urlpatterns()
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

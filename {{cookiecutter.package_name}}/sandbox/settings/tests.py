"""
Django settings for tests
"""
from sandbox.settings.base import *  # noqa: F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Media directory dedicated to tests to avoid polluting other environment
# media directory
MEDIA_ROOT = VAR_PATH / "media-tests"  # noqa: F405
{% if cookiecutter.include_cmsplugin|lower == 'true' %}
# Available CMS page template for tests purposes only
TEST_PAGE_TEMPLATE = "pages/test.html"
CMS_TEMPLATES.append(  # noqa: F405
    (TEST_PAGE_TEMPLATE, "test-basic"),
)
{% endif %}
# Disable every cache because it can trouble test on expected results
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

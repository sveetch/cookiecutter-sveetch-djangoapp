import os
import shutil
import sys


# API option value, cleaned and lowercase so it should be safe for wrong input
ENABLE_DRF = "{{ cookiecutter.enable_drf }}".lower().strip()


# Various paths related to API feature
PROJECT_API_PATHS = [
    "{{ cookiecutter.app_name }}/serializers/",
    "{{ cookiecutter.app_name }}/viewsets/",
    "{{ cookiecutter.app_name }}/routers.py",
    "docs/django_app/serializers.rst",
    "docs/django_app/viewsets.rst",
    "tests/100_serializers/",
    "tests/110_viewsets/",
]


def clean_api_parts(paths):
    """
    Clean generated project from every paths related to API feature.

    Keywords Arguments:
        paths (list): List of relative (to generated project root) path to remove.
    """
    for path in paths:
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)


# Only "true" (don't matter it's lower or upper case from user input) value is
# considered to enable option, any other value will assume to disable option.
if ENABLE_DRF != "true":
    clean_api_parts(PROJECT_API_PATHS)

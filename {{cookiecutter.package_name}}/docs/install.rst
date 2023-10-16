.. _intro_install:

=======
Install
=======

Install package in your environment : ::

    pip install {{ cookiecutter.package_name }}

For development usage see :ref:`install_development`.

Configuration
*************

Add it to your installed Django apps in settings : ::

    INSTALLED_APPS = (
        ...{% if cookiecutter.include_api|lower == 'true' %}
        "rest_framework",{% endif %}
        "{{ cookiecutter.app_name }}",
    )

Then load default application settings in your settings file: ::

    from {{ cookiecutter.app_name }}.settings import *

Then mount applications URLs: ::

    urlpatterns = [
        ...
        path("", include("{{ cookiecutter.app_name }}.urls")),
    ]

And finally apply database migrations.

Settings
********

.. automodule:: {{ cookiecutter.app_name }}.settings
   :members:

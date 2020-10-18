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
        ...
        '{{ cookiecutter.app_name }}',
    )

Then load its settings from your settings file: ::

    from {{ cookiecutter.app_name }}.settings import *

And finally apply database migrations.

Settings
********

These are the default settings you can override in your own project settings
right after the line which load the default app settings.

.. automodule:: {{ cookiecutter.app_name }}.settings
   :members:

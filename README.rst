.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Python: https://www.python.org
.. _virtualenv: https://virtualenv.pypa.io
.. _pip: https://pip.pypa.io
.. _Pytest: http://pytest.org
.. _Napoleon: https://sphinxcontrib-napoleon.readthedocs.org
.. _Flake8: http://flake8.readthedocs.org
.. _Sphinx: http://www.sphinx-doc.org
.. _tox: http://tox.readthedocs.io
.. _livereload: https://livereload.readthedocs.io
.. _Read the Docs: https://readthedocs.org/
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
.. _twine: https://twine.readthedocs.io
.. _Django REST Framework: https://www.django-rest-framework.org/

==============================
cookiecutter-sveetch-djangoapp
==============================

Yet another `Cookiecutter`_ template to produce a repository to start
a Django application package with Python3.

It emphases on simple package with quality and not any relation to
any service (state badge, pyup, travis, etc..) except `Read the Docs`_
link in README.

A sample built from this template is available on repository
`sveetch-djangoapp-sample <https://github.com/sveetch/sveetch-djangoapp-sample>`_.
Note that this is a version with every options enabled and its version may not always
match this template current version (mostly if there is no major feature).

Package content
***************

A Django package with everything to start:

* Development in a Python virtual environment with `virtualenv`_ and `pip`_;
* Promote Test Driven Development with `Pytest`_;
* Latest Django versions support;
* Configuration in ``setup.cfg`` ready to release on Pypi;
* Clean application structure per model;
* Sample blog application (very minimalist) with test coverage;
* Optionnal API with `Django REST Framework`_ with test coverage;
* `Flake8`_ configuration for quality review;
* `tox`_ configuration for environments tests;
* Code is fully documented with `reStructuredText`_ and `Napoleon`_
  extension for `Sphinx`_.
* Release with `twine`_.

Package cover some basic features:

* A very minimalist Blog application for sample;
* Basic generic views usage;
* Basic API (if enabled) with routers, serializers and viewsets;
* Testing models, factories and views;
* pyquery usage for tests on HTML contents;

Usage
*****

Just invoke the `Cookiecutter`_ template to create a new project: ::

    cookiecutter https://github.com/sveetch/cookiecutter-sveetch-djangoapp.git

.. warning::

    Django 4.0 support is enabled by default but it drops Python3.7, however you can
    disable it to keep Python3.7 support, see Options section below for more details.


Package requirements
--------------------

To use it from repository url you just need `Cookiecutter`_ version 1.6 or 1.7.

.. note::

    We are awaiting Cookiecutter 2.x stable release to migrate.


Once project is created, you can install it locally with ``make install``
from project directory.

However you can install this cookie locally (to avoid doing request each time
you use it), you will need virtualenv, clone it where you want and use its
``make install`` command. Once installed you can create shortcut with a bash
alias in your ``.bash_aliases``: ::

    alias cookdjango='/home/your/install/cookiecutter-sveetch-django/.venv/bin/cookiecutter /home/your/install/cookiecutter-sveetch-django'

Options
-------

You can define author full name, email, github username, pypi username,
version start, package name and package short description.

Some of these have a default value filled from a previous value, obviously
you can edit it to your own needs.

You can pre define some options in your
`cookiecutter user configuration <https://cookiecutter.readthedocs.io/en/1.7.2/advanced/user_config.html>`_
to avoid to input them each time you use this cookie. This is especially
recommended for the author and username ones.

Special options
...............

``enable_drf``
    This is to enable API feature with Django REST framework. It is enabled by default and
    it expect a ``True`` or ``true`` value, any other value will disable feature.

``django_4_support``
    This is a new temporary option which is true by default. If you enable it, your
    project will have Django 4.0 support but this drop Python3.7 support since
    Django 4.0 does not support it anymore.

    If you need Python3.7, you need to disable this option (answer anything else than
    ``true``) but obviously you will lose Django 4.0 support.

    This option is temporary and may sooner be removed along Python3.7 support in
    profit of Django 4.x support.

About first project install
---------------------------

Created application have models but no migrations. This is to avoid creating
migration for models you will surely change or remove.

This will result in failures on tests and running application until you
have created initial migrations. There is a makefile action for this: ::

    make migrations

It will automatically search to create new migrations for your application
if there is some changes or new models. When done, there is a makefile
action to apply new migrations: ::

    make migrate

So if you just plan to check created package, just performs migration
creation. However if you plan to create your own application, create your
models and make migrations once finished.

But remember than until you've done migrations, tests will fail.

Naming
******

For a given ``Sample bar`` project name:

* Package name will be ``sample-bar``;
* Application name will ``sample_bar``;

You can change package and application names during project creation.

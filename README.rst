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
.. _Click: https://click.palletsprojects.com
.. _Read the Docs: https://readthedocs.org/
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
.. _twine: https://twine.readthedocs.io

==============================
cookiecutter-sveetch-djangoapp
==============================

Yet another `Cookiecutter`_ template to produce a repository to start
a Django application package with Python3.

It emphases on simple package with quality and not any relation to
any service (state badge, pyup, travis, etc..) except `Read the Docs`_
link in README.

TODO: A sample built from this template is available on repository
`sveetch-djangoapp-sample <https://github.com/sveetch/sveetch-djangoapp-sample>`_.

Usage
*****

Just invoke the `Cookiecutter`_ template to create a new project: ::

    cookiecutter https://github.com/sveetch/cookiecutter-sveetch-djangoapp.git

Package content
    A Python3 package with everything to start:

    * Development in a Python virtual environment with `virtualenv`_ and `pip`_;
    * Promote Test Driven Development with `Pytest`_;
    * Configuration in ``setup.cfg`` ready to upload package to Pypi;
    * Sample object to say hello world;
    * `Flake8`_ configuration for quality review;
    * Tests on sample object;
    * `tox`_ configuration for tests;
    * Code is fully documented with `reStructuredText`_ and `Napoleon`_
      extension for `Sphinx`_.
    * Release with `twine`_.

    Package cover some basic features:

    * Object inheritance;
    * Python logging usage;
    * Testing core, command line and logging;

TODO: About first project install
    Created project have models but no migrations. This is to avoid creating
    migration for models you will surely change or remove.

    This will result in failures on tests and running application until you
    have created initial migrations. There is a makefile action for this: ::

        make migrations

    Will automatically search to create new migrations for your application
    if there is some changes or new models. When done, there is makefile action
    to apply new migrations: ::

        make migrate

Package requirements
    To use it from repository url you just need `Cookiecutter`_.

    However if you want to install it locally (to avoid doing request each time
    you use it) you will need virtualenv and use the ``make install`` from
    template Makefile. Once installed you can create a bash alias like: ::

        alias cookpy='/home/your/install/cookiecutter-sveetch-python/.venv/bin/cookiecutter /home/your/install/cookiecutter-sveetch-python'

    Once created, you can install it locally with ``make install`` from project
    directory.

Naming
    For a given ``Sample bar`` project name:

    * Package name will be ``sample-bar``;
    * Application name will ``sample_bar``;

    You can change package and application names during project creation.

Options
    You can define author full name, email, github username, pypi username,
    version start, package name and package short description.

    Some of these have a default value filled from a previous value, obviously
    you can edit it to your own needs.

    You can pre define some options in your
    `cookiecutter user configuration <https://cookiecutter.readthedocs.io/en/1.7.2/advanced/user_config.html>`_
    to avoid to input it each time. This is especially recommended for the
    author and username ones.

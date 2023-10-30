.. _usage_intro:

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
.. _Bootstrap: https://getbootstrap.com/

=======
Options
=======

You can define author full name, email, github username, pypi username,
version start, package name and package short description.

You can pre define some option values in your
`cookiecutter user configuration <https://cookiecutter.readthedocs.io/en/1.7.2/advanced/user_config.html>`_
to avoid input them each time you use this cookie. This is especially
recommended for the author and username that are pretty common on cookiecutter
templates.


Naming
******

Project name
    The full project name which is used as the package, the README and documentation
    titles. You should avoid to input a title longer than 35 characters.

    Cookiecutter variable name: ``project_name``.

Project short description
    The description used in package and README. This is a short description, you should
    avoid to input a description longer than 55 characters.

    Cookiecutter variable name: ``project_short_description``.

Application name
    The Python module name that will hold application code. Default value will be the
    project name slugified. It must be a valid Python identifier (no special character,
    no unicode, no whitespace).

    Cookiecutter variable name: ``app_name``.

Package name
    The Python package name. Default value will be the project name slugified. It must
    be a valid Python package name. (no special character, no unicode, no whitespace,
    no ``-``).

    Cookiecutter variable name: ``package_name``.


Authoring
*********

Author name
    The author name to use in credits and package metas.

    Cookiecutter variable name: ``author_name``.

Author email
    The author email to use in credits and package metas.

    Cookiecutter variable name: ``author_email``.

Author username
    The author username is mostly used to build the Github repository URL.

    Cookiecutter variable name: ``author_username``.

Username for Pypi
    The username used to release package on the
    `Python Package Index <https://pypi.org/>`_, you will need an account on it.

    Cookiecutter variable name: ``pypi_username``.


Git repository
**************

If enabled, your new project will be initialized as a Git repository and everything
will be added to an initial commit. It is enabled by default.

This is useful to quickly start playing on your new project in a new branch and be
able to goes back to initial state.

Cookiecutter variable name: ``init_git_repository``.


API with Django REST framework
******************************

This is to enable API feature with Django REST framework. It is enabled by default.

Cookiecutter variable name: ``include_api``.


Plugin for DjangoCMS
********************

This is to enable DjangoCMS configuration and add a plugin for a sample model.

The application will be slightly different since DjangoCMS involves some
additional things to work like i18n url, to be mounted at root of sandbox, a
homepage, templates, etc..

Cookiecutter variable name: ``include_cmsplugin``.


Modern frontend
***************

This will include a frontend configuration inside project. Makefile
will have some additional tasks to install and build frontend. Sandbox skeleton
template will load frontend CSS and JS assets.

This is a pretty basic frontend with Node.js, Babel, Webpack, jQuery, Sass compiler
and Bootstrap. It will be enough to prototype your layout but you will probably
need to improve it yourself for more specific usecases.

Cookiecutter variable name: ``include_frontend``.

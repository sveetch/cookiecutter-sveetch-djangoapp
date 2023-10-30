.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/stable/
.. _virtualenv: https://virtualenv.pypa.io
.. _pip: https://pip.pypa.io

.. _usage_intro:

=====
Usage
=====

.. _usage_quickstart:

Quickstart
**********

To use this template to create a new project you just need to install `Cookiecutter`_
version 2.1.0 or latter then use it directly from its repository URL: ::

    cookiecutter https://github.com/sveetch/cookiecutter-sveetch-djangoapp.git


.. _usage_install:

Install
*******

To speed up project creation you may install this cookie on your system.

First ensure you have `pip`_ and `virtualenv`_ packages installed and *GNU make*
available on your system. Then type: ::

    git clone https://github.com/sveetch/cookiecutter-sveetch-djangoapp.git
    cd cookiecutter-sveetch-djangoapp
    make install

.. Warning::

    You will need to update your template install yourself opposed to the direct
    repository usage (:ref:`usage_quickstart`) which always try to use the
    latest version from the master branch.


Makefile task
-------------

You can use the Makefile task: ::

    make project

It will create all new project in ``dist/`` directory.


Bash alias
----------

Once installed you can also create shortcut with a bash alias in your
``.bash_aliases``: ::

    alias cookdjangoapp='/home/your/install/cookiecutter-sveetch-djangoapp/.venv/bin/cookiecutter /home/your/install/cookiecutter-sveetch-djangoapp'

So you will just have to execute following command to create a new project: ::

    cookdjangoapp


About first project install
***************************

Created application will have models but no migrations. This is to avoid creating
migration for models you will surely change or remove.

This will result in failures on tests and running application until you
have created initial migrations. There is a makefile action for this: ::

    make migrations

It will automatically search to create new migrations for your application
if there is some changes or new models. When done, there is a makefile
action to apply new migrations: ::

    make migrate

Remember than until you've done migrations, the tests will fail. So if you just plan
to check created package, you can use the following commands: ::

    make install migrations quality
    make migrate

Don't merge the line within the first one, it won't work.

.. Hint::
    If you plan to create your own application models, you will create them and
    only make migrations once you have finished.

    If you enabled the Git repository initialization option, you can create the dummy
    migrations, play with project and easily back to initial state to start working
    with empty migrations, just remember you will have to remove the previous database
    to avoid migration conflicts.

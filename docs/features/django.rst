.. Attention::

    We are currently working to finish this documentation.

.. _features_django_intro:

======
Django
======

Generated application implements a very basic Blog. Its only purpose is to demonstrate
a full Django application with fundamental parts.

Module index
************

Each module directory have a ``__init__.py`` file with a ``__all__`` to define a list
of public objects of that module.

Its primarily goal here is to declare commonly exposed objects and reduce import lines.

For the following structure: ::

    foo/
    ├── bar
    │   ├── __init__.py
    │   └── ping.py
    └── __init__.py

With a ``Pong`` class object in ``ping.py``, you would normally import it with: ::

    from foo.bar.ping import Pong

But if ``bar/__init__.py`` defines the ``Pong`` class in ``__all__`` you may be able
to import it with: ::

    from foo.bar import Pong

This is especially useful for application part like models, views, etc.. to expose
concrete object commonly used outside.

Don't formalize on this hint, if you don't plan to use and maintain it, remove them
and import everything with a direct import (but you will need to update internal
imports from generated application).

URLs
****

File ``urls.py`` from application set a variable ``app_name`` to define
`URL namespace <https://docs.djangoproject.com/en/4.2/topics/http/urls/#url-namespaces>`_
so all URL resolving will have to use it, you can see an example of this in models
methods ``get_absolute_url``.

All URL are defined with a simple path (``django.urls.path``), because we try avoid to
use Regex path (``re_path``) that should be restricted to specific use cases. Simple
path is more easy to use than Regex because of
`Path converters <https://docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters>`_,
when you need a specific converter it is easy to
`define a custom converter <https://docs.djangoproject.com/en/4.2/topics/http/urls/#registering-custom-path-converters>`_.


Views
*****

All views are
`Class-based views <https://docs.djangoproject.com/en/4.2/topics/class-based-views/>`_
because View functions are monolithic and not flexible enough for real life projects.

The Django documentation about Class-based views is complete but can be troubling
when searching for inheritances and feature methods, so you should bookmark the
`Class-based view Inspector <https://ccbv.co.uk/>`_ that is very helpful.


Models
******

Included models are very basic but at least you will notice they all define a
method ``get_absolute_url()`` that is something you should always define properly in
your models.


Template
********

Included templates are very basic. Remember to always procuce valid HTML and properly
define blocks like ``{% block app_content %}{% endblock app_content %}`` (note the name
on the ``endblock``, this is to enforce readability).


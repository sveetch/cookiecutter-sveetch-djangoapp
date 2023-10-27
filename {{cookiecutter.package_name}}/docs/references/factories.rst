.. _references_factories:

=========
Factories
=========

These are the model object factories made with
`factory_boy <https://factoryboy.readthedocs.io/>`_ and to be used in tests to ease
model object creation.

.. automodule:: {{ cookiecutter.app_name }}.factories.article
    :members: ArticleFactory
    :undoc-members:

.. automodule:: {{ cookiecutter.app_name }}.factories.blog
    :members: BlogFactory{% if cookiecutter.include_cmsplugin %}, BlogPluginModelFactory{% endif %}
    :undoc-members:

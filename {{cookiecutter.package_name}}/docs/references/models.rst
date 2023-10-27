.. _references_models:

======
Models
======

These are the `Django model <https://docs.djangoproject.com/en/4.2/topics/db/models/>`_
object definitions used in application with Django ORM.

.. automodule:: {{ cookiecutter.app_name }}.models.article
    :members: Article
    :exclude-members: DoesNotExist, MultipleObjectsReturned

.. automodule:: {{ cookiecutter.app_name }}.models.blog
    :members: Blog{% if cookiecutter.include_cmsplugin %}, BlogPluginModel{% endif %}
    :exclude-members: DoesNotExist, MultipleObjectsReturned

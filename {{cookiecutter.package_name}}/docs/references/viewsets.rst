.. _references_viewsets:

========
Viewsets
========

These are the
`DRF viewsets <https://www.django-rest-framework.org/api-guide/viewsets/>`_ used to
implement API endpoints.

.. automodule:: {{ cookiecutter.app_name }}.viewsets.article
    :members: ArticleViewSet

.. automodule:: {{ cookiecutter.app_name }}.viewsets.blog
    :members: BlogViewSet

.. automodule:: {{ cookiecutter.app_name }}.viewsets.mixins
    :members: ConditionalResumedSerializerMixin

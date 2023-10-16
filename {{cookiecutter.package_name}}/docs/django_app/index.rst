.. _intro_django-app:

==================
Django application
==================

.. toctree::
   :maxdepth: 2

   models.rst{% if cookiecutter.include_api|lower == 'true' %}
   serializers.rst
   viewsets.rst{% endif %}

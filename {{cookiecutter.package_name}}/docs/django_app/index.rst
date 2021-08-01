.. _intro_django-app:

==================
Django application
==================

.. toctree::
   :maxdepth: 2

   models.rst{% if cookiecutter.enable_drf|lower == 'true' %}
   serializers.rst
   viewsets.rst{% endif %}

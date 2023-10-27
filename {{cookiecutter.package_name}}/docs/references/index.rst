.. _references_intro:

==========
References
==========

.. toctree::
   :maxdepth: 2

   factories.rst
   models.rst{% if cookiecutter.include_cmsplugin %}
   plugins.rst{% endif %}{% if cookiecutter.include_api %}
   serializers.rst{% endif %}
   views.rst{% if cookiecutter.include_api %}
   viewsets.rst{% endif %}

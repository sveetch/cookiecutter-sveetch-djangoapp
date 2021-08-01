.. _Python: https://www.python.org
.. _Django: https://www.djangoproject.com/
.. _Django REST framework: https://www.django-rest-framework.org/

.. {{ cookiecutter.package_name }} documentation master file, created by {{ cookiecutter.author_name }}

{{ '=' * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

{{ cookiecutter.project_short_description|wordwrap(80) }}

Dependancies
************

* `Python`_>=3.6;
* `Django`_>=2.2;{% if cookiecutter.enable_drf|lower == 'true' %}
* `Django REST framework`_>=3.12.0;{% endif %}

Links
*****

* Read the documentation on `Read the docs <https://{{ cookiecutter.package_name }}.readthedocs.io/>`_;
* Download its `PyPi package <https://pypi.python.org/pypi/{{ cookiecutter.package_name }}>`_;
* Clone it on its `Github repository <https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.package_name }}>`_;

User’s Guide
************

.. toctree::
   :maxdepth: 2

   install.rst
   django_app/index.rst

Developer’s Guide
*****************

.. toctree::
   :maxdepth: 1

   development.rst
   history.rst

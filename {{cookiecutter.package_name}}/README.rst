.. _Python: https://www.python.org/
.. _Django: https://www.djangoproject.com/{% if cookiecutter.enable_drf|lower == 'true' %}
.. _Django REST framework: https://www.django-rest-framework.org/{% endif %}

{{ '=' * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

{{ cookiecutter.project_short_description|wordwrap(80) }}

Dependancies
************

* `Python`_>={% if cookiecutter.django_4_support|lower == 'true' %}3.7{% else %}3.6{% endif %};
* `Django`_{% if cookiecutter.django_4_support|lower == 'true' %}>=2.2,<4.1{% else %}>=2.2,<4.0{% endif %};{% if cookiecutter.enable_drf|lower == 'true' %}
* `Django REST framework`_>=3.13.1;{% endif %}

Links
*****

* Read the documentation on `Read the docs <https://{{ cookiecutter.package_name }}.readthedocs.io/>`_;
* Download its `PyPi package <https://pypi.python.org/pypi/{{ cookiecutter.package_name }}>`_;
* Clone it on its `Github repository <https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.package_name }}>`_;

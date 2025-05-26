.. _Python: https://www.python.org/
.. _Django: https://www.djangoproject.com/{% if cookiecutter.include_api %}
.. _Django REST framework: https://www.django-rest-framework.org/{% endif %}{% if cookiecutter.include_cmsplugin %}
.. _DjangoCMS: https://docs.django-cms.org/{% endif %}

{{ '=' * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

{{ cookiecutter.project_short_description|wordwrap(80) }}


Dependencies
************

* `Python`_>=3.10;
* `Django`_>=4.2;{% if cookiecutter.include_api %}
* `Django REST framework`_>=3.16.0;{% endif %}{% if cookiecutter.include_cmsplugin %}
* `DjangoCMS`_>5.0.0;{% endif %}


Links
*****

* Read the documentation on `Read the docs <https://{{ cookiecutter.package_name }}.readthedocs.io/>`_;
* Download its `PyPi package <https://pypi.python.org/pypi/{{ cookiecutter.package_name }}>`_;
* Clone it on its `Github repository <https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.package_name }}>`_;

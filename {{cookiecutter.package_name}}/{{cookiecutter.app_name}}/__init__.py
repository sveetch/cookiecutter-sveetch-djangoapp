"""{{ cookiecutter.project_short_description|wordwrap(80) }}"""
from importlib.metadata import version


__pkgname__ = "{{ cookiecutter.package_name }}"
__version__ = version(__pkgname__)

"""A system to compose project parts from applications enabled in a manifest"""
from importlib.metadata import version


__pkgname__ = "{{ cookiecutter.package_name }}"
__version__ = version(__pkgname__)

"""
Pytest fixtures
"""
from pathlib import Path

import pytest

import {{ cookiecutter.app_name }}


class FixturesSettingsTestMixin(object):
    """
    A mixin containing settings about application. This is almost about useful
    paths which may be used in tests.

    Attributes:
        application_path (pathlib.Path): Absolute path to the application directory.{% if cookiecutter.include_cmsplugin %}
        application_urlpath (pathlib.Path): URL path to the application as mounted
            in project ``urls.py``.{% endif %}
        package_path (pathlib.Path): Absolute path to the package directory.
        tests_dir (pathlib.Path): Directory name which include tests.
        tests_path (pathlib.Path): Absolute path to the tests directory.
        fixtures_dir (pathlib.Path): Directory name which include tests datas.
        fixtures_path (pathlib.Path): Absolute path to the tests datas.
    """
    def __init__(self):
        self.application_path = Path(
            {{ cookiecutter.app_name }}.__file__
        ).parents[0].resolve()
        self.application_urlpath = "{% if cookiecutter.include_cmsplugin %}{{ cookiecutter.app_name }}{% endif %}"

        self.package_path = self.application_path.parent

        self.tests_dir = "tests"
        self.tests_path = self.package_path / self.tests_dir

        self.fixtures_dir = "data_fixtures"
        self.fixtures_path = self.tests_path / self.fixtures_dir

    def format(self, content):
        """
        Format given string to include some values related to this application.

        Arguments:
            content (str): Content string to format with possible values.

        Returns:
            str: Given string formatted with possible values.
        """
        return content.format(
            HOMEDIR=Path.home(),
            PACKAGE=str(self.package_path),
            APPLICATION=str(self.application_path),{% if cookiecutter.include_cmsplugin %}
            URLPATH=str(self.application_urlpath),{% endif %}
            TESTS=str(self.tests_path),
            FIXTURES=str(self.fixtures_path),
            VERSION={{ cookiecutter.app_name }}.__version__,
        )


@pytest.fixture(scope="function")
def temp_builds_dir(tmp_path):
    """
    Prepare a temporary build directory.

    NOTE: You should use directly the "tmp_path" fixture in your tests.
    """
    return tmp_path


@pytest.fixture(scope="module")
def tests_settings():
    """
    Initialize and return settings for tests.

    Example:
        You may use it in tests like this: ::

            def test_foo(tests_settings):
                print(tests_settings.package_path)
                print(tests_settings.format("Application version: {VERSION}"))
    """
    return FixturesSettingsTestMixin()

from django.apps import AppConfig


class {{ cookiecutter.app_name }}Config(AppConfig):
    name = "{{ cookiecutter.app_name }}"
    verbose_name = "{{ cookiecutter.project_name }}"
    default_auto_field = "django.db.models.AutoField"

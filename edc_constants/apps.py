from django.apps import AppConfig as DjangoAppConfig
from django.core.checks.registry import register

from .system_checks import context_processors_check


class AppConfig(DjangoAppConfig):
    name = "edc_constants"
    verbose_name = "Edc Constants"

    def ready(self):
        register(context_processors_check)

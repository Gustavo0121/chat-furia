"""Apps."""

from django.apps import AppConfig


class BackendConfig(AppConfig):
    """BackendConfig."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'

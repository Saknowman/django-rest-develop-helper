from django.apps import AppConfig


class EntityConfig(AppConfig):
    name = 'entity'

    def ready(self):
        from . import signals

from django.apps import AppConfig
from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
            import user.signals


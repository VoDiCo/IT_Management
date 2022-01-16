from django.apps import AppConfig


class DeviceManagmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'device_management'

    def ready(self):
        import device_management.signals
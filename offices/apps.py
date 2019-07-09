from django.apps import AppConfig


class OfficesConfig(AppConfig):
    name = 'offices'

    def ready(self):
        import offices.signals

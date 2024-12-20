from django.apps import AppConfig


class BookinServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bookin_service"

    def ready(self) -> None:
        import bookin_service.signal
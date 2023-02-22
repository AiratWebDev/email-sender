from .celery import app as celery_app

__all__ = ('celery_app',)  # добавим, чтобы убедиться, что celery будет запускаться при запуске проекта
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_redis_emails.settings')  # убеждаемся, что файл с настройками доступен
# через ключ DJANGO_SETTINGS_MODULE

app = Celery('celery_redis_emails')  # указываем имя основного модуля в проекте в качестве контекста
app.config_from_object('django.conf:settings',
                       namespace='CELERY')  # указываем, что нужные команды в настройках будут начинаться с префикса CELERY

app.conf.enable_utc = False

app.conf.update(timezone='Europe/Paris')

app.autodiscover_tasks()  # автоматически находим все задачи в проекте

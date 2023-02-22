from time import sleep
from celery import shared_task
from django.core.mail import send_mail
from celery_redis_emails import settings


@shared_task(serializer='json', name="send_mail")
def send_feedback_email_task(email, message):
    sleep(15)
    send_mail(
        'Заголовок письма',
        f'Тело письма, полученного из формы. Сообщение — {message}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

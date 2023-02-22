from django import forms
from .tasks import send_feedback_email_task
from celery_redis_emails.secret_info import SENDER


class SubscribeForm(forms.Form):
    email = forms.EmailField(label='Почтовый адрес')
    message = forms.CharField(label="Ваше сообщение",
                              widget=forms.Textarea(attrs={'rows': '7'}))

    def send_email(self):
        """Отправляем email, когда форма будет отправлена"""
        send_feedback_email_task.delay(self.cleaned_data['email'], self.cleaned_data['message'])


    # def send_email(self):
    #     """Отправляем email, когда форма будет отправлена без использования Celery"""
    #     sleep(20)
    #     send_mail(
    #         'Заголовок письма',
    #         f'Тело письма, полученного из формы. Сообщение — {self.cleaned_data["message"]}',
    #         SENDER,
    #         [self.cleaned_data['email']],
    #         fail_silently=False,
    #     )

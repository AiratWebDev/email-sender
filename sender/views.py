from django.views.generic.edit import FormView
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import SubscribeForm
from celery_redis_emails.secret_info import EMAILS, SENDER


class FormPageView(FormView):
    template_name = 'subscription.html'
    form_class = SubscribeForm
    success_url = 'done'

    def form_valid(self, form):
        """Функция вызывается при успешной отправке формы"""
        form.send_email()
        return super().form_valid(form)


def send_email(request):
    # html_info = render_to_string('template_example.html', {'context': 'values'}, request)
    send_mail(
        'Заголовок письма',
        'Тело письма',
        SENDER,
        [EMAILS],
        fail_silently=False,
        # html_message=html_info,
    )
    return render(request, 'sended.html')


def done_page(request):
    return render(request, 'sended.html')

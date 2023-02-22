from django.urls import path
from .views import send_email, done_page, FormPageView

urlpatterns = [
    path('send', send_email),
    path('done', done_page),
    path('', FormPageView.as_view()),
]

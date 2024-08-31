from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'task4'
urlpatterns = [
    # представления поста
    path('', views.sign_up_by_html),
    path('django_sign_up/', views.sign_up_by_django),
]

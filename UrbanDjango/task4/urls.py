from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'task4'
urlpatterns = [
    # представления поста

    path('platform/', TemplateView.as_view(template_name='fourth_task/platform.html')),
    path('games/', views.games, name='task4/games'),
    path('cart/', views.cart, name='task4/cart'),
]

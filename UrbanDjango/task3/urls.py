from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'task3'
urlpatterns = [
    # представления поста

    path('platform/', TemplateView.as_view(template_name='third_task/platform.html')),
    # path('newspaper/', views.np_release, name='task3/func'),
    path('games/', views.games, name='task3/games'),
    path('cart/', views.cart, name='task3/cart'),
    # path('release/', np_release),
    # path('team/', np_team)
]

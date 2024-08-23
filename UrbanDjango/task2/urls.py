from django.urls import path
from . import views

app_name = 'task2'
urlpatterns = [
    # представления поста
    path('', views.task2_func, name='task2/func'),
    path('class/', views.task2_class.as_view(), name='task2/class'),
]

from django.urls import path
from . import views
from .views import post_list

urlpatterns = [
    path('', views.index, name='index'),  # Пример маршрута
]
from django.urls import path
from .views import post_list

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    ...
]

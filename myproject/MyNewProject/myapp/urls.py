from django.urls import path
from . import views
from django.urls import path
urlpatterns = [
    path('text/', views.text_response, name='text_response'),
    path('html/', views.html_response, name='html_response'),
]


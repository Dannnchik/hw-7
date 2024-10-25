from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
from django.urls import path
from .views import profile_view, post_edit

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    ...
]

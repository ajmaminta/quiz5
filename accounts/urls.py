# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_users'),
    path('users/<int:user_id>/', views.get_user, name='get_user'),
]

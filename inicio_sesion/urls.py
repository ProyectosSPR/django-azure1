from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect


urlpatterns = [
    path('', views.profile, name='root'),
    path('registrar/', views.registrar, name='registrar'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_custom, name='logout'),
    path('profile/', views.profile, name='profile'),
]
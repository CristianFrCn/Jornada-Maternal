from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
]

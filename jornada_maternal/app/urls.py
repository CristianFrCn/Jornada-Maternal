from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.site, name='site'),
    path('login/', views.login, name='login'),
    path('redefenir/', views.redefenir, name='redefenir' ),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('vacina/', views.vacina, name='vacina'),
    path('prenatal/', views.prenatal, name='prenatal'),
    path('mais/', views.mais, name='mais'),
    path('amamentacao/', views.amamentacao, name='amamentacao'),
     path('chat/', views.chat, name='chat'),
    path('noticias/', views.noticias, name='noticias'),

    ]

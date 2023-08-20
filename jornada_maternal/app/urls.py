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
    path('create_adicionais', views.create_adicionais, name='create_adicionais'),
    path('read_adicionais', views.read_adicionais, name='read_adicionais'),
    path("update_adicionais/<int:id>", views.update_adicionais, name='update_adicionais'),
    path("delete_adicionais/<int:id>", views.delete_adicionais, name='delete_adicionais'),

    ]

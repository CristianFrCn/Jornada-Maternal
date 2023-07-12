from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redefenir/', views.redefenir, name='redefenir' ),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('inicio/', views.inicio, name='inicio'),
    path('abaVacina/', views.abaVacina, name='abaVacina'),
    path('abaPreNatal/', views.abaPreNatal, name='abaVacina'),
    path('abaMais/', views.abaMais, name='abaMais'),
    path('subAmamentacao/', views.subAmamentacao, name='subAmamentacao'),
    path('subNoticias/', views.subNoticias, name='subNoticias'),

    ]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .viewsets import ClienteViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet, basename="Cliente")

urlpatterns = [
    path('', views.site, name='site'),
    path('login/', views.login, name='login'),
    path('login/redefenir/', views.redefenir, name='redefenir' ),
    path('login/cadastro/', views.cadastro, name='cadastro'),
    path('vacina/', views.vacina, name='vacina'),
    path('prenatal/', views.prenatal, name='prenatal'),
    path('informacoes/', views.informacoes, name='informacoes'),
    path('mais/', views.mais, name='mais'),
    path('amamentacao/', views.amamentacao, name='amamentacao'),
    path('chat/', views.chat, name='chat'),
    path('noticias/', views.noticias, name='noticias'),

    path('informacoes/vacina/', views.vacina, name='vacina'),
    path('informacoes/prenatal', views.prenatal, name='prenatal'),

    path('chat/site/', views.site, name='site'),
    path('login/redefenir/site/', views.site, name='site'),

    path('menu', views.menu, name='menu'),


    path('create_cliente', views.create_cliente, name='create_cliente'),
    path('read_cliente', views.read_cliente, name='read_cliente'),
    path("update_cliente/<int:id>", views.update_cliente, name='update_cliente'),
    path("delete_cliente/<int:id>", views.delete_cliente, name='delete_cliente'),



    ]

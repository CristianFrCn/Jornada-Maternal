from django.contrib import admin
from django.urls import path
from .rest_framework import routers
from .viewsets import GestanteViewSet
from . import views


router = routers.DefaultRouts()
router = f

urlpatterns = [
    path("cep/<int:id>", views.cep, name='cep'),
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
    path('create_Gestante', views.create_Gestante, name='create_Gestante'),
    path('read_Gestante', views.read_Gestante, name='read_Gestante'),
    path("update_Gestante/<int:id>", views.update_Gestante, name='update_Gestante'),
    path("delete_Gestante/<int:id>", views.delete_Gestante, name='delete_Gestante'),



    ]

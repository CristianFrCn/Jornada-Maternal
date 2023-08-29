from django.forms import ModelForm
from django import forms
from .models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','datanascimento','cpf','idadecrianca',
                  'sus','estado','cidade','nomecrianca','generocrianca',]
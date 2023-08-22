from django.forms import ModelForm
from django import forms
from .models import Gestante

class GestanteForm(ModelForm):
    class Meta:
        model = Gestante
        fields = ['nome', 'cpf', 'idade','sus','endereco','genero','crianca']
from datetime import date

from django.db import models
from django import forms
#class User(models.Model):
   # user_nickname = models.CharField(max_length=100, primary_key=True, default='')
   # user_nome = models.CharField(max_length=150, default = '')
  #  user_email = models.EmailField(default='')
   # user_age = models.IntegerField(default = '0')

   # def __str__(self):
     #   return f'Nickname : {self.user_nickname} | E-mail: {self.user_email}'
class ClienteForm(forms.ModelForm):
    datanascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class Cliente(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    nome = models.CharField(max_length=40, verbose_name='Nome')
    datanascimento = models.DateField(verbose_name='Data de Nascimento, digite com a "/"')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    idadecrianca = models.IntegerField(verbose_name='Idade da Criança')
    sus = models.CharField(max_length=16, verbose_name='Número SUS')
    endereco = models.CharField(max_length=50, verbose_name='Endereco')
    bairro = models.CharField(max_length=70, verbose_name='Bairro')
    cep = models.CharField(max_length=15, verbose_name='Cep')
    cidade = models.CharField(max_length=30, verbose_name='Cidade')
    uf = models.CharField(max_length=30, verbose_name='Uf')
    nomecrianca = models.CharField(max_length=40, verbose_name='Nome da Criança')
    generocrianca = models.CharField(max_length=1, choices=GENERO_CHOICES, verbose_name='Gênero da Criança')


    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"
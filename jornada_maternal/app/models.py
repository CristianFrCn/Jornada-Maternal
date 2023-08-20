from django.db import models
class Gestante(models.Model):
    nome  = models.CharField(max_length=40)
    cpf= models.CharField(max_length=11)
    idade = models.IntegerField()
    sus = models.CharField(max_length=15)
    endereco = models.CharField(max_length=70)
    genero = models.CharField(max_length=1)
    crianca = models.CharField(max_length=40)
    def __str__(self):
        return self.cpf

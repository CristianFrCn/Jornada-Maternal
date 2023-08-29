from django.db import models
class Cliente(models.Model):
    nome  = models.CharField(max_length=40)
    datanascimento = models.CharField(max_length=40)
    cpf= models.CharField(max_length=11)
    idadecrianca = models.IntegerField()
    sus = models.CharField(max_length=15)
    estado = models.CharField(max_length=15)
    cidade = models.CharField(max_length=70)
    nomecrianca = models.CharField(max_length=40)
    generocrianca = models.CharField(max_length=1)

    def __str__(self):
        return self.cpf + ' - ' + self.nome

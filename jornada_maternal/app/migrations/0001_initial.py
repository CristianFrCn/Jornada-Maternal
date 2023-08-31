# Generated by Django 4.2.4 on 2023-08-31 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('datanascimento', models.DateField(verbose_name='Data de Nascimento, digite com a "/"')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('idadecrianca', models.IntegerField(verbose_name='Idade da Criança')),
                ('sus', models.CharField(max_length=16, verbose_name='Número SUS')),
                ('endereco', models.CharField(max_length=9, verbose_name='Endereco')),
                ('bairro', models.CharField(max_length=70, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=15, verbose_name='Cep')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=30, verbose_name='Uf')),
                ('nomecrianca', models.CharField(max_length=40, verbose_name='Nome da Criança')),
                ('generocrianca', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Gênero da Criança')),
            ],
        ),
    ]

from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')

class Fotografo(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')

class Estudio(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

class SessaoFoto(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    tipo = models.CharField(max_length=50)
    duracao = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=7,decimal_places=2)
    finalizado = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fotografo = models.ForeignKey(Fotografo, on_delete=models.PROTECT)
    estudio = models.ForeignKey(Estudio, on_delete=models.PROTECT)


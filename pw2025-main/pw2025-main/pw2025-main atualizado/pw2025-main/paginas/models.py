from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(verbose_name="E-mail")
      
    def __str__(self):
        return f"{self.telefone}"
       
    def __str__(self):
        return f"{self.email}"
 
    def __str__(self):
        return f"{self.nome}"


class Fotografo(models.Model):
    nome = models.CharField(max_length=100,verbose_name="Nome")
    especialidade = models.CharField(max_length=100, verbose_name="Especialidade")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")

    def __str__(self):
        return f"{self.telefone}"
       
    def __str__(self):
        return f"{self.especialidade}"
 
    def __str__(self):
        return f"{self.nome}"

class Estudio(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    endereco = models.CharField(max_length=200, verbose_name="Endereco")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")

    def __str__(self):
        return f"{self.telefone}"
       
    def __str__(self):
        return f"{self.endereco}"
 
    def __str__(self):
        return f"{self.nome}"

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


from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Address(models.Model):
   cep = models.CharField(max_length=10)
   endereco = models.CharField(max_length=100)
   numero = models.IntegerField()
   complemento = models.CharField(max_length=50)
   bairro = models.CharField(max_length=100)
   cidade = models.CharField(max_length=100)
   uf = models.CharField(max_length=2)
   descricao = models.CharField(max_length=100)

from django.db import models
from .endereco import Endereco

class Fabricante(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.ManyToManyField(Endereco, related_name="endereco_fabricante", blank=True)
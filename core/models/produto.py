from django.db import models
from .fabricante import Fabricante

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.ManyToManyField(Fabricante, related_name="produtos", blank=True)
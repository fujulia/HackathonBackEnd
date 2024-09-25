from django.db import models
from .fabricante import Fabricante

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    garantia_meses = models.IntegerField(default=0,  null=True, blank=True)
    fabricantes = models.ManyToManyField(Fabricante, related_name="produto_fabricante", blank=True)
  
  
    def __str__(self):
       return self.nome
  

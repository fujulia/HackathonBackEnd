from django.db import models
from .endereco import Endereco
from .telefone import Telefone

class Fabricante(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.IntegerField(default=0,  null=False, blank=False)
    email = models.EmailField(max_length=200, null=True, blank=True)
    site = models.URLField(max_length=200, blank=True, null=True)
    endereco = models.ManyToManyField(Endereco, related_name="endereco_fabricante", blank=True)
    telefone =  models.ManyToManyField(Telefone, related_name="telefone_fabricante", blank=True)
    
      
    def __str__(self):
       return self.nome
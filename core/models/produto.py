from django.db import models
from .fabricante import Fabricante
from uploader.models import Image
from .categoria import Categoria

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False, blank=False)
    descricao = models.JSONField(null=True)
    garantia_meses = models.IntegerField(default=0,  null=True, blank=True)
    fabricante = models.ManyToManyField(Fabricante, related_name="produto_fabricante", blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="categoria", null=True, blank=True )
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    foto = models.ManyToManyField(
        Image,
        related_name="produto_foto",
        null=True,
        blank=True,
        default=None,
    )
    
  
    def __str__(self):
       return self.nome
  

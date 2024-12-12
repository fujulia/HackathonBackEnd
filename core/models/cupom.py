from django.db import models
from .user import User

class Cupom(models.Model):
    nome = models.CharField(max_length=100)
    porcentagem_desconto = models.DecimalField(max_digits=3, decimal_places=2, default=0, null=False, blank=False)
    
    def __str__(self):
     return self.nome
  

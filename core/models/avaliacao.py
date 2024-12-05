from django.db import models
from django.utils import timezone
from .user import User
from .produto import Produto


class Avaliacao(models.Model):
   usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="avaliacao", null=True, blank=True)
   produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="produto_avaliacao", null=True, blank=True)
   nota = models.IntegerField(  null=False, blank=False)
   comentario = models.CharField(max_length=500, null=True, blank=True)
   data = models.DateTimeField(default=timezone.now)
  
   def __str__(self):
    return f'{self.usuario} - {self.nota}'
  

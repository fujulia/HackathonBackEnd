from django.db import models 
from .user import User
from django.utils import timezone

class Orcamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orcamento", null=True, blank=True)
    consumoMensal = models.DecimalField(max_digits=10, decimal_places=2)
    gastoSemPlaca = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=255, null=False, blank=True)
    irradiacao = models.DecimalField(max_digits=10, decimal_places=2)
    potenciaPlaca = models. DecimalField(max_digits=10, decimal_places=5)
    areaDisponivel = models.DecimalField(max_digits=10, decimal_places=2)
    gastoComPlaca = models.DecimalField(max_digits=10, decimal_places=2)
    playback = models.DecimalField(max_digits=10, decimal_places=1)
    porcetangemReducao = models.DecimalField(max_digits=10, decimal_places=2)
    qtdPlaca = models.IntegerField(null=True, blank=True)
    data = models.DateTimeField(default=timezone.now)
     
     
    def __str__(self):
       return f'({self.usuario}) {self.data}'
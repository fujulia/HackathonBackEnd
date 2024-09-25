from django.db import models

class Endereco(models.Model):
    estado = models.CharField(max_length=255, null=False, blank=True)
    cidade = models.CharField(max_length=255, null=False, blank=True)
    bairro = models.CharField(max_length=100, null=False, blank=True)
    rua = models.CharField(max_length=255, null=False, blank=True)
    numero = models.IntegerField(default=0,  null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=8)
    
    def __str__(self):
        return f"{self.rua} {self.numero} ({self.bairro})"
from django.db import models


class Despesa(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False, blank=False)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.valor} ({self.data})"
    
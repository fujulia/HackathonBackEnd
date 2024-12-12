from django.db import models 
from django.db.models.signals import post_save
from django.dispatch import receiver
from .despesa import Despesa
from .compra import Compra

class MovimentacaoFinanceira(models.Model):
    class Tipo(models.IntegerChoices):
        ENTRADA = 1, "Entrada"
        SAÍDA = 2, "Saída"
        
    tipo = models.IntegerField(choices=Tipo.choices)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.valor} ({self.Tipo(self.tipo).label})"
    
    
    
# @receiver(post_save, sender=Compra)
# def criar_movimentacao_entrada(sender, instance, created, **kwargs):
#     if created:
#         MovimentacaoFinanceira.objects.create(
#             tipo=1,
#             valor=instance.total,
#             descricao=f"Venda de {instance.produto.nome}",
#         )

@receiver(post_save, sender=Despesa)
def criar_movimentacao_saida(sender, instance, created, **kwargs):
    if created:
        MovimentacaoFinanceira.objects.create(
            tipo=2,
            valor=instance.valor,
            descricao=instance.descricao,
        )
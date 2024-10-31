from django.db import models
from django.utils import timezone
from .user import User
from .produto import Produto


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    class MetodoPagamento(models.IntegerChoices):
        PIX = 1, "Pix"
        CARTAO = 2, "Cartão"
        
        
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compra", null=True, blank=True)
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    metodo_Pagamento = models.IntegerField(choices=MetodoPagamento.choices, default=MetodoPagamento.PIX)
    data = models.DateTimeField(default=timezone.now)
    
    
    @property
    def total(self):
        return sum(item.preco * item.quantidade for item in self.itens.all())

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)

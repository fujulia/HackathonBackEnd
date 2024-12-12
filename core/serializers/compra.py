from rest_framework.serializers import (
    CharField,
    CurrentUserDefault, #
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    DateTimeField,
)

from core.models import Compra, ItensCompra
from .cupom import CupomSerializer
from django.db import transaction
        
class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.produto.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade", "total")
        depth = 1

class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade")
    
    def validate_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValidationError("A quantidade deve ser maior do que zero.")
        return quantidade

    def validate(self, item):
        if item["quantidade"] > item["produto"].quantidade:
            raise ValidationError("Quantidade de itens maior do que a quantidade em estoque.")
        return item

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(read_only=True, many=True)
    data = DateTimeField(read_only=True) 
    tipo_pagamento = CharField(source="get_tipo_pagamento_display", read_only=True)
    cupom = CupomSerializer(read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "data", "tipo_pagamento", "itens", "cupom", "desconto")
        

class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True) # Aqui mudou
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        cupom = validated_data.pop("cupom", None)

        with transaction.atomic():
            compra = Compra.objects.create(**validated_data, cupom=cupom)

            # Criação dos itens da compra
            for item_data in itens_data:
                item_data["preco"] = item_data["produto"].preco
                ItensCompra.objects.create(compra=compra, **item_data)

            compra.total()  # Atualiza o total após a criação
        return compra
    
    
    def update(self, compra, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            compra.itens.all().delete()
            for item in itens:
                item["preco"] = item["produto"].preco  # nova linha
                ItensCompra.objects.create(compra=compra, **item)
        cupom = validated_data.get("cupom", None)
        compra.cupom = cupom  # Atualiza o cupom
        compra.total()
        compra.save()
        return super().update(compra, validated_data)
    
    
#listar compras 

class ListarItensCompraSerializer(ModelSerializer):
    produto = CharField(source="produto.nome", read_only=True)

    class Meta:
        model = ItensCompra
        fields = ("quantidade", "produto")
        depth = 1


class ListarCompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ListarItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "itens")
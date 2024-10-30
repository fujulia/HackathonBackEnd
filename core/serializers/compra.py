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

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "data", "tipo_pagamento", "itens")
        

class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True) # Aqui mudou
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            item["preco"] = item["produto"].preco # nova linha
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra
    
    
    def update(self, compra, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            compra.itens.all().delete()
            for item in itens:
                item["preco"] = item["produto"].preco  # nova linha
                ItensCompra.objects.create(compra=compra, **item)
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
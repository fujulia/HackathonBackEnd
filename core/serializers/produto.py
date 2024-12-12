from rest_framework.serializers import (
    DecimalField,
    ModelSerializer,
    Serializer,
    SlugRelatedField,
    ValidationError,
)
from rest_framework import serializers
from core.models import Produto

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
    

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1
        
class AlterarPrecoSerializer(serializers.Serializer):
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_preco(self, value):
        """Valida se o preço é um valor positivo."""
        if value <= 0:
            raise serializers.ValidationError("O preço deve ser um valor positivo.")
        return value
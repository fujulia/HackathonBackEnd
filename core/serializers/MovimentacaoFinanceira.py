from rest_framework.serializers import ModelSerializer

from core.models import MovimentacaoFinanceira

class MovimentacaoSerializer(ModelSerializer):
    class Meta:
        model = MovimentacaoFinanceira
        fields = "__all__"
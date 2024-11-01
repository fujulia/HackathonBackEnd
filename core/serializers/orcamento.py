from rest_framework.serializers import ModelSerializer

from core.models import Orcamento

class OrcamentoSerializer(ModelSerializer):
    class Meta:
        model = Orcamento
        fields = "__all__"
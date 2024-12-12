from rest_framework.serializers import ModelSerializer

from core.models import Despesa

class DespesaSerializer(ModelSerializer):
    class Meta:
        model = Despesa
        fields = "__all__"
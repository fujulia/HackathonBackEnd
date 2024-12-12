from rest_framework.serializers import ModelSerializer

from core.models import Telefone

class TelefoneSerializer(ModelSerializer):
    class Meta:
        model = Telefone
        fields = "__all__"
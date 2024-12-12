from rest_framework.serializers import ModelSerializer

from core.models import Cupom

class CupomSerializer(ModelSerializer):
    class Meta:
        model = Cupom
        fields = "__all__"
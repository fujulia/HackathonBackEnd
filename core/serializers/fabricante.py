from rest_framework.serializers import ModelSerializer

from core.models import Fabricante

class FabricanteSerializer(ModelSerializer):
    class Meta:
        model = Fabricante
        fields = "__all__"
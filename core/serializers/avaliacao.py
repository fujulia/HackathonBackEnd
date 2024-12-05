from rest_framework.serializers import ModelSerializer

from core.models import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = "__all__"
        
class AvaliacaoDetailSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = "__all__"
        depth = 2
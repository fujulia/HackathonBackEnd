from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Avaliacao
from core.serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["usuario", "produto_nome" , "nota", "data"]
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Orcamento
from core.serializers import  OrcamentoSerializer

class OrcamentoViewSet(ModelViewSet):
    queryset = Orcamento.objects.all()
    serializer_class = OrcamentoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["usuario", "data" , "estado"]
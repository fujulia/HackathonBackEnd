from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.models import MovimentacaoFinanceira
from core.serializers import MovimentacaoSerializer

class MovimentacaoViewSet(ModelViewSet):
    queryset = MovimentacaoFinanceira.objects.all()
    serializer_class = MovimentacaoSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["tipo", "data"]
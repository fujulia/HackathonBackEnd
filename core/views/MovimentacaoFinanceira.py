from rest_framework.viewsets import ModelViewSet

from core.models import MovimentacaoFinanceira
from core.serializers import MovimentacaoSerializer

class MovimentacaoViewSet(ModelViewSet):
    queryset = MovimentacaoFinanceira.objects.all()
    serializer_class = MovimentacaoSerializer
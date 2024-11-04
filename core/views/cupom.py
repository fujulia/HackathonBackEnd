from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Cupom
from core.serializers import CupomSerializer

class CupomViewSet(ModelViewSet):
    queryset = Cupom.objects.all()
    serializer_class = CupomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nome", "porcentagem_desconto"]
from rest_framework.viewsets import ModelViewSet

from core.models import Fabricante
from core.serializers import FabricanteSerializer
from django_filters.rest_framework import DjangoFilterBackend

class FabricanteViewSet(ModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nome", "cnpj" , "email"]

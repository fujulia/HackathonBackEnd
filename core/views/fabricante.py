from rest_framework.viewsets import ModelViewSet

from core.models import Fabricante
from core.serializers import FabricanteSerializer

class FabricanteViewSet(ModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
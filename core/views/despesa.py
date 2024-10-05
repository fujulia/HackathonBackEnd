from rest_framework.viewsets import ModelViewSet

from core.models import Despesa
from core.serializers import DespesaSerializer

class DespesaViewSet(ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
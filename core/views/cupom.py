from rest_framework.viewsets import ModelViewSet

from core.models import Cupom
from core.serializers import CupomSerializer

class CupomViewSet(ModelViewSet):
    queryset = Cupom.objects.all()
    serializer_class = CupomSerializer
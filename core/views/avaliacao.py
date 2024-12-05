from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Avaliacao
from core.serializers import AvaliacaoSerializer, AvaliacaoDetailSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [AllowAny]  # Permite acesso sem autenticação
    authentication_classes = [] 
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["usuario", "produto_nome" , "nota", "data"]
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return AvaliacaoDetailSerializer
        return AvaliacaoSerializer
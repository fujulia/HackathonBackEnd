from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import ProdutoSerializer, ProdutoDetailSerializer, AlterarPrecoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProdutoDetailSerializer
        return ProdutoSerializer
    
    
    @action(detail=True, methods=["patch"])
    def alterar_preco(self, request, pk=None):
        produto = self.get_object()

        serializer = AlterarPrecoSerializer(data=request.data)

        if serializer.is_valid():
            produto.preco = serializer.validated_data["preco"]
            produto.save()

            return Response(
                {"detail": f"Preço do produto '{produto.titulo}' atualizado para {produto.preco}."}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
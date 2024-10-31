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
        # Busca o livro pelo ID usando self.get_object()
        produto = self.get_object()

        # Obtém o novo preço do corpo da requisição
        novo_preco = request.data.get("preco")

        # Verifica se o preço foi fornecido e se é um número válido
        if novo_preco is None:
            return Response({"detail": "O preço é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            novo_preco = float(novo_preco)
        except ValueError:
            return Response({"detail": "O preço deve ser um número válido."}, status=status.HTTP_400_BAD_REQUEST)

        # Atualiza o preço do livro e salva
        produto.preco = novo_preco
        produto.save()

        # Retorna uma resposta de sucesso
        return Response(
            {"detail": f"Preço do produto '{produto.titulo}' atualizado para {produto.preco}."}, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["post"])
    def ajustar_estoque(self, request, pk=None):
        # Recupera o livro pelo ID usando self.get_object()
        produto = self.get_object()

        # Recupera o valor de ajuste passado no body da requisição
        quantidade_ajuste = request.data.get("quantidade")

        if quantidade_ajuste is None:
            return Response(
                {"erro": "Por favor, informe uma quantidade para ajustar."}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Tenta converter o valor para um número inteiro
            quantidade_ajuste = int(quantidade_ajuste)
        except ValueError:
            return Response(
                {"erro": "O valor de ajuste deve ser um número inteiro."}, status=status.HTTP_400_BAD_REQUEST
            )

        # Atualiza a quantidade em estoque
        produto.quantidade += quantidade_ajuste

        # Garante que o estoque não seja negativo
        if produto.quantidade < 0:
            return Response(
                {"erro": "A quantidade em estoque não pode ser negativa."}, status=status.HTTP_400_BAD_REQUEST
            )

        # Salva as alterações no banco de dados
        produto.save()

        # Retorna uma resposta com o novo valor em estoque
        return Response(
            {"status": "Quantidade ajustada com sucesso", "novo_estoque": produto.quantidade}, status=status.HTTP_200_OK
        )
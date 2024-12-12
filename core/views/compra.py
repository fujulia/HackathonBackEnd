from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from core.models import Compra, Cupom
from core.serializers import CompraSerializer, CriarEditarCompraSerializer, ListarCompraSerializer
from django.db import transaction

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    authentication_classes = [] 

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["usuario", "status" , "metodo_Pagamento", "data", "cupom_nome"]
    
    
    # def get_queryset(self):
    #     usuario = self.request.user
    #     if usuario.is_superuser:
    #         return Compra.objects.all()
    #     if usuario.groups.filter(name="Administradores"):
    #         return Compra.objects.all()
    #     return Compra.objects.filter(usuario=usuario)

    def get_serializer_class(self):
        if self.action == "list":
            return ListarCompraSerializer
        if self.action in ("create", "update"):
            return CriarEditarCompraSerializer
        return CompraSerializer
    
    
    @action(detail=True, methods=["post"])
    def finalizar(self, request, pk=None):
        # Recupera o objeto 'compra' usando self.get_object(), com base no pk fornecido.
        compra = self.get_object()

        # Verifica se o status da compra é diferente de 'CARRINHO'.
        # Se não for, a compra já foi finalizada e não pode ser finalizada novamente.
        if compra.status != Compra.StatusCompra.CARRINHO:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"status": "Compra já finalizada"},
            )

        # Abre uma transação atômica para garantir que todas as operações no banco
        # de dados ocorram de forma consistente (ou todas são salvas ou nenhuma).
        with transaction.atomic():
            
            cupom_nome = request.data.get("cupom", "").upper()
            
            if cupom_nome:
            # Busca o cupom na tabela, verifica se está ativo e se ainda é válido
                cupom = Cupom.objects.filter(nome=cupom_nome).first()
                if cupom:
                    # Aplica o desconto da tabela Cupom
                    compra.cupom = cupom
                    compra.desconto = cupom.porcentagem_desconto * 100  # Armazena o valor do desconto na compra
                else:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={"status": "Cupom inválido ou expirado"}
                    )
                
            # Itera sobre todos os itens da compra.
            for item in compra.itens.all():

                # Verifica se a quantidade de um item é maior que a quantidade disponível no estoque do livro.
                if item.quantidade > item.produto.quantidade:
                    # Se a quantidade solicitada for maior que o estoque disponível, retorna um erro.
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={
                            "status": "Quantidade insuficiente",  # Mensagem de erro
                            "livro": item.produto.nome,  # Informa qual livro tem estoque insuficiente
                            "quantidade_disponivel": item.produto.quantidade,  # Mostra a quantidade disponível
                        },
                    )

                # Se o estoque for suficiente, subtrai a quantidade do item do estoque do livro.
                item.produto.quantidade -= item.quantidade
                # Salva as alterações no livro (atualiza o estoque no banco de dados).
                item.produto.save()

            # Após todos os itens serem processados e o estoque ser atualizado,
            # atualiza o status da compra para 'REALIZADO'.
            compra.status = Compra.StatusCompra.REALIZADO
            # Salva as alterações da compra no banco de dados.
            compra.save()

        # Retorna uma resposta de sucesso indicando que a compra foi finalizada.
        return Response(status=status.HTTP_200_OK, data={"status": "Compra finalizada"})
    
    
    @action(detail=False, methods=["get"])
    def relatorio_vendas_mes(self, request):
        # Define o início do mês atual
        agora = timezone.now()
        inicio_mes = agora.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        # Filtra as compras realizadas desde o início do mês até o presente momento
        compras = Compra.objects.filter(status=Compra.StatusCompra.REALIZADO, data__gte=inicio_mes)

        # Calcula o total de vendas e a quantidade de vendas
        total_vendas = sum(compra.total for compra in compras)
        quantidade_vendas = compras.count()

        # Retorna o relatório
        return Response(
            {
                "status": "Relatório de vendas deste mês",
                "total_vendas": total_vendas,
                "quantidade_vendas": quantidade_vendas,
            },
            status=status.HTTP_200_OK,
        )
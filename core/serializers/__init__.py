from .user import UserSerializer
from .produto import ProdutoSerializer, ProdutoDetailSerializer, AlterarPrecoSerializer
from .fabricante import FabricanteSerializer
from .avaliacao import AvaliacaoSerializer
from .endereco import EnderecoSerializer
from .telefone import TelefoneSerializer
from .despesa import DespesaSerializer
from .cupom import CupomSerializer
from .compra import (
    CompraSerializer,
    CriarEditarCompraSerializer,
    ListarCompraSerializer,
    ItensCompraSerializer,
    CriarEditarItensCompraSerializer,
    ListarItensCompraSerializer, 
)
from .MovimentacaoFinanceira import MovimentacaoSerializer
from .orcamento import OrcamentoSerializer
from .categoria import CategoriaSerializer

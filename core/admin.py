"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
from core.models import Produto, Avaliacao, Compra, Cupom, Despesa, Endereco, Fabricante, MovimentacaoFinanceira, Telefone, User, Categoria, ItensCompra, Orcamento


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name", "passage_id", "telefone", "endereco","foto")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
        (_("Groups"), {"fields": ("groups",)}),
        (_("User Permissions"), {"fields": ("user_permissions",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    # "telefone",
                    # "endereco",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','categoria', 'preco')
    search_fields = ('nome','categoria', 'preco')
    list_filter = ('nome','categoria', 'preco')
    ordering = ('nome','categoria', 'preco')
    list_per_page = 10

@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'email')
    search_fields = ('nome', 'cnpj', 'email')
    list_filter = ('nome', 'cnpj', 'email')
    ordering = ('nome', 'cnpj', 'email')
    list_per_page = 10

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua','estado','cidade', 'bairro', 'numero')
    search_fields = ('rua','estado','cidade', 'bairro', 'numero')
    list_filter = ('rua','estado','cidade', 'bairro', 'numero')
    ordering = ('rua','estado','cidade', 'bairro', 'numero')
    list_per_page = 10

@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('numero','ddd')
    search_fields = ('numero','ddd')
    list_filter = ('numero','ddd')
    ordering = ('numero','ddd')
    list_per_page = 10
    
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario','produto', 'nota')
    search_fields = ('usuario','produto', 'nota')
    list_filter = ('usuario','produto', 'nota')
    ordering = ('usuario','produto', 'nota')
    list_per_page = 10
    
@admin.register(Cupom)
class CupomAdmin(admin.ModelAdmin):
    list_display = ('nome','porcentagem_desconto')
    search_fields = ('nome','porcentagem_desconto')
    list_filter = ('nome','porcentagem_desconto')
    ordering = ('nome','porcentagem_desconto')
    list_per_page = 10
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao')
    search_fields = ('nome','descricao')
    list_filter = ('nome','descricao')
    ordering = ('nome','descricao')
    list_per_page = 10
  
@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('valor','descricao')
    search_fields = ('valor','descricao')
    list_filter = ('valor','descricao')
    ordering = ('valor','descricao')
    list_per_page = 10  
    
@admin.register(MovimentacaoFinanceira)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'valor', 'descricao')
    search_fields = ('tipo', 'valor', 'descricao')
    list_filter = ('tipo', 'valor', 'descricao')
    ordering = ('tipo', 'valor', 'descricao')
    list_per_page = 10  
    
    
class ItensCompraInline(admin.TabularInline):
    model = ItensCompra
    extra = 1 


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("usuario", "status")
    search_fields = ("usuario", "status")
    list_filter = ("usuario", "status")
    ordering = ("usuario", "status")
    list_per_page = 25
    inlines = [ItensCompraInline]


@admin.register(Orcamento)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("usuario", "data")
    search_fields = ("usuario", "data")
    list_filter = ("usuario", "data")
    ordering = ("usuario", "data")
    list_per_page = 25






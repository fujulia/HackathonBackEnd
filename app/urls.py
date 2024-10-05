from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from django.conf import settings
from core.views import UserViewSet, ProdutoViewSet, FabricanteViewSet, AvaliacaoViewSet, EnderecoViewSet, TelefoneViewSet, DespesaViewSet, CupomViewSet, CompraViewSet, MovimentacaoViewSet

router = DefaultRouter()

router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"produtos", ProdutoViewSet)
router.register(r"fabricantes", FabricanteViewSet)
router.register(r"avaliacoes", AvaliacaoViewSet)
router.register(r"enderecos", EnderecoViewSet)
router.register(r"telefones", TelefoneViewSet)
router.register(r"despesas", DespesaViewSet)
router.register(r"cupons", CupomViewSet)
router.register(r"compras", CompraViewSet)
router.register(r"movimentacoes", MovimentacaoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Simple JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # images
    path("api/media/", include(uploader_router.urls)),
    # API
    path("api/", include(router.urls)),

]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)

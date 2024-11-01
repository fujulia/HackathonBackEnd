from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from passageidentity import Passage, PassageError
from passageidentity.openapi_client.models import UserInfo
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import Group

from core.models import User  # Use apenas esta importação se `User` está em core.models

# Configurações do Passage
PASSAGE_APP_ID = settings.PASSAGE_APP_ID
PASSAGE_API_KEY = settings.PASSAGE_API_KEY
PASSAGE_AUTH_STRATEGY = settings.PASSAGE_AUTH_STRATEGY
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY, auth_strategy=PASSAGE_AUTH_STRATEGY)


class TokenAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = "core.authentication.TokenAuthentication"
    name = "tokenAuth"
    match_subclasses = True
    priority = -1

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name="Authorization",
            token_prefix="Bearer",
        )


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request) -> tuple[User, None]:
        if not request.headers.get("Authorization"):
            return None

        psg_user_id: str = self._get_user_id(request)
        user: User = self._get_or_create_user(psg_user_id)

        return (user, None)

    def _get_or_create_user(self, psg_user_id) -> User:
        try:
            # Busca o usuário existente
            user: User = User.objects.get(passage_id=psg_user_id)
            self._promote_if_admin(user)  # Promove se necessário
            return user
        except ObjectDoesNotExist:
            # Cria novo usuário se não encontrado
            try:
                psg_user: UserInfo = psg.getUser(psg_user_id)
                user: User = User.objects.create_user(
                    passage_id=psg_user.id,
                    email=psg_user.email,
                )
                self._promote_if_admin(user)  # Promove se necessário
                return user
            except PassageError as e:
                raise AuthenticationFailed("Erro ao obter informações do usuário do Passage.") from e

    def _promote_if_admin(self, user: User) -> None:
        if user.email in settings.ADMIN_EMAILS:
            group, created = Group.objects.get_or_create(name=settings.ADMIN_GROUP_NAME)
            user.groups.add(group)  # Adiciona ao grupo
            if not user.is_staff or not user.is_superuser:
                user.is_staff = True
                user.is_superuser = True
                user.save()  # Salva as alterações
                print(f"Usuário {user.email} promovido a admin e adicionado ao grupo 'Administradores'.")
        else:
            group, created = Group.objects.get_or_create(name=settings.COMPRADOR_GROUP_NAME)
            user.groups.add(group) 
            user.save()

    def _get_user_id(self, request) -> str:
        try:
            psg_user_id: str = psg.authenticateRequest(request)
        except PassageError as e:
            raise AuthenticationFailed("Falha na autenticação do token.") from e

        return psg_user_id

from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import models
from django.utils import timezone
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User


class SnippetViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manipulação de snippets
    Fornece automaticamente as ações 'list', 'create', 'retrieve',
    'update' e 'destroy'
    """

    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Personaliza a queryset para:
        1. Não mostrar snippets expirados
        2. Filtrar snippets privados para apenas seus donos
        """
        queryset = Snippet.objects.all()

        # Remove snippets expirados
        queryset = queryset.filter(
            models.Q(expires_at__isnull=True) | models.Q(expires_at__gt=timezone.now())
        )

        # Filtra snippets privados
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(is_private=False)
        else:
            queryset = queryset.filter(
                models.Q(is_private=False) | models.Q(owner=self.request.user)
            )

        return queryset

    def perform_create(self, serializer):
        """
        Quando criar um novo snippet, define o usuário atual como dono
        """
        serializer.save(owner=self.request.user)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        """
        Endpoint adicional para retornar o código highlighted em HTML
        """
        snippet = self.get_object()
        return Response(snippet.highlighted)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para visualização de usuários
    Apenas leitura - não permite criação/edição via API
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

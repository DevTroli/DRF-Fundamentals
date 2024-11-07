from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer


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


class SnippetListView(ListView):
    model = Snippet
    template_name = "snippets/list.html"
    context_object_name = "snippets"
    paginate_by = 12

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                models.Q(is_private=False)
                | models.Q(
                    owner=self.request.user
                    if self.request.user.is_authenticated
                    else None
                )
            )
        )


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = "snippets/detail.html"
    context_object_name = "snippet"

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(is_private=False)
        return queryset


class SnippetCreateView(LoginRequiredMixin, CreateView):
    model = Snippet
    success_url = reverse_lazy("snippet-list")
    template_name = "snippets/form.html"
    fields = [
        "title",
        "code",
        "language",
        "style",
        "expires_at",
        "is_private",
        "linenos",
    ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class SnippetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Snippet
    template_name = "snippets/form.html"
    fields = [
        "title",
        "code",
        "language",
        "style",
        "expires_at",
        "is_private",
        "linenos",
    ]

    def test_func(self):
        snippet = self.get_object()
        return snippet.owner == self.request.user


class SnippetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Snippet
    template_name = "snippets/confirm_delete.html"
    success_url = reverse_lazy("snippet-list")

    def test_func(self):
        snippet = self.get_object()
        return snippet.owner == self.request.user


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona o usuário logado e os snippets dele ao contexto
        context["user"] = self.request.user
        context["snippets"] = Snippet.objects.filter(owner=self.request.user)
        return context


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para visualização de usuários
    Apenas leitura - não permite criação/edição via API
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Cria um router e registra nossos viewsets
router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet)

# URLs da API são determinadas automaticamente pelo router
urlpatterns = [
    path("", include(router.urls)),
]

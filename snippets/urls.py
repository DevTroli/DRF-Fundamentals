from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as v

# Router para API endpoints
router = DefaultRouter()
router.register(r"api/snippets", v.SnippetViewSet, basename="api-snippet")
router.register(r"api/users", v.UserViewSet)

# URLs para views baseadas em templates
template_patterns = [
    path("", v.SnippetListView.as_view(), name="snippet-list"),
    path("snippets/new/", v.SnippetCreateView.as_view(), name="snippet-create"),
    path("snippets/<int:pk>/", v.SnippetDetailView.as_view(), name="snippet-detail"),
    path(
        "snippets/<int:pk>/edit/",
        v.SnippetUpdateView.as_view(),
        name="snippet-update",
    ),
    path(
        "snippets/<int:pk>/delete/",
        v.SnippetDeleteView.as_view(),
        name="snippet-delete",
    ),
    path("profile/", v.ProfileView.as_view(), name="profile"),
]

urlpatterns = template_patterns + router.urls

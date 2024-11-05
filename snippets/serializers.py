from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer para converter snippets em JSON e vice-versa
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    highlighted = serializers.ReadOnlyField()

    class Meta:
        model = Snippet
        fields = [
            "id",
            "title",
            "code",
            "created",
            "expires_at",
            "is_private",
            "linenos",
            "language",
            "style",
            "owner",
            "highlighted",
        ]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para informações básicas do usuário
    """

    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]

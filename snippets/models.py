from django.db import models
from django.contrib.auth.models import User
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

# Obtém todas as linguagens suportadas pelo Pygments
LEXERS = [item for item in get_all_lexers() if item[1]]
# Cria uma lista de tuplas (identificador, nome_amigável) para as linguagens
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# Obtém todos os estilos de highlighting disponíveis
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    """
    Modelo principal para armazenar trechos de código (snippets)
    """

    # Campos básicos
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    # Campos para controle de expiração e visibilidade
    expires_at = models.DateTimeField(null=True, blank=True)
    is_private = models.BooleanField(default=False)

    # Campos para syntax highlighting
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)

    # Campos para rastreamento
    owner = models.ForeignKey(User, related_name="snippets", on_delete=models.CASCADE)
    highlighted = models.TextField(blank=True)

    class Meta:
        ordering = ["created"]

    def save(self, *args, **kwargs):
        """
        Sobrescrevemos o método save para gerar o código highlighted
        sempre que um snippet for salvo
        """
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        formatter = HtmlFormatter(style=self.style, linenos=linenos)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

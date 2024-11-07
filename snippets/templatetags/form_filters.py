from django import template

register = template.Library()


@register.filter(name="addclass")
def addclass(field, css_class):
    """
    Template filter para adicionar classes CSS aos campos de formulário
    Uso: {{ form.field|addclass:"class-name" }}
    """
    return field.as_widget(attrs={"class": css_class})

# finance/templatetags/custom_filters.py
from django import template

register = template.Library()


@register.filter
def moeda_br(valor):
    """Formata valor para moeda brasileira"""
    try:
        valor = float(valor)
        formatado = (
            f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        )
        return f"R$ {formatado}"
    except (ValueError, TypeError):
        return valor

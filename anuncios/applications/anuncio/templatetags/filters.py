import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def resaltar_texto(value):
    lista_words = re.findall("[#]\w+", value)
    for word in lista_words:
        value = value.replace(
            word,
            '<strong style="color: blue;">%s</strong>' % (word)
        )
    return mark_safe(value)

@register.filter(name="precio")
def redondear_precio(number):
  return round(number, 2)
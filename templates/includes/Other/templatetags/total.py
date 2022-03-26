
from django import template
register = template.Library()

@register.simple_tag
def total(price, piece, quan):
    try:
        return (int(price) / int(piece)) * int(quan)
    except (ValueError, ZeroDivisionError):
        return None


# register.filter('total', total)
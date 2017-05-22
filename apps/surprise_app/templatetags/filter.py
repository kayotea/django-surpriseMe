from django import template
register = template.Library()

@register.filter 
def slice_to(value, upto):
    try:
        return value[:upto]
    except:
        return None
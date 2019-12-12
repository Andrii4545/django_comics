from django import template

register = template.Library()

# Create your views here.
@register.simple_tag
def query_update(query, key, value):
    query = query.copy()
    query[key] = value
    return query.urlencode()

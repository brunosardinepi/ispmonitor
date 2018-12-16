from django import template

from ispmonitor import settings


register = template.Library()

@register.filter
def ip_address_to_slug(ip_address):
    if ip_address:
        return ip_address.replace(".", "-")

@register.simple_tag
def use_ga():
    return settings.USE_GA

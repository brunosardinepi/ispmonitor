from django import template

register = template.Library()


@register.filter
def ip_address_to_slug(ip_address):
    return ip_address.replace(".", "-")

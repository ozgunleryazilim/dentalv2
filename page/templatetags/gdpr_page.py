from django import template
from page.models import GDPRPageSeo

register = template.Library()


@register.simple_tag
def get_gdpr_obj():
    return GDPRPageSeo.objects.first()

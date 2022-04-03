from django import template
from page.models import AboutPageSeo

register = template.Library()


@register.simple_tag
def get_about_obj():
    return AboutPageSeo.objects.first()

from django import template
from page.models import HomePageSeo

register = template.Library()


@register.simple_tag
def get_home_obj():
    return HomePageSeo.objects.first()

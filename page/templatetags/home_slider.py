from django import template
from page.models import HomeSlider

register = template.Library()


@register.simple_tag
def get_slider_list():
    return HomeSlider.objects.all()

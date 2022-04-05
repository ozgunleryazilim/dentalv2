from django import template
from page.models import HowItWorksPageSeo

register = template.Library()


@register.simple_tag
def get_howitworks_seo():
    return HowItWorksPageSeo.objects.first()

from django import template
from page.models import ContactPageSeo

register = template.Library()


@register.simple_tag
def get_contact_obj():
    return ContactPageSeo.objects.first()

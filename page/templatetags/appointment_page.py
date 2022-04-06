from django import template
from page.models import AppointmentPageSeo

register = template.Library()


@register.simple_tag
def get_appointment_obj():
    return AppointmentPageSeo.objects.first()

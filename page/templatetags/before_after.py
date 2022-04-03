from django import template
from page.models import BeforeAfterImage

register = template.Library()


@register.simple_tag
def get_before_after_images():
    return BeforeAfterImage.objects.all()

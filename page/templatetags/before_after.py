from django import template
from page.models import BeforeAfterImage, BeforeAfterPageSeo

register = template.Library()


@register.simple_tag
def get_before_after_images():
    return BeforeAfterImage.objects.all()


@register.simple_tag
def get_before_after_seo():
    return BeforeAfterPageSeo.objects.first()

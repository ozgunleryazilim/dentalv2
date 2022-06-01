from django.conf import settings
from django import template

register = template.Library()


@register.simple_tag
def get_recaptcha_site_key():
    return settings.RECAPTCHA_SITE_KEY


@register.simple_tag
def get_recaptcha_secret_key():
    return settings.RECAPTCHA_SECRET_KEY


@register.simple_tag
def get_recaptcha_validation_active():
    return settings.RECAPTCHA_VALIDATION_ACTIVE

import requests
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def recaptcha_check(recaptcha_response):
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    value = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    response = requests.post(verify_url, value)
    result = response.json()
    return result['success']


def validate_recaptcha(data):
    if not settings.RECAPTCHA_VALIDATION_ACTIVE:
        return

    recaptcha_response = data.get('g-recaptcha-response')
    recaptcha_response_result = recaptcha_check(recaptcha_response)

    if not recaptcha_response_result:
        raise ValidationError(_("Recaptcha doğrulaması başarısız"))

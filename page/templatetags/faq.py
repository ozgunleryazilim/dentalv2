from django import template
from page.models import FrequentlyAskedQuestion

register = template.Library()


@register.simple_tag
def get_faq_list():
    return FrequentlyAskedQuestion.objects.all()

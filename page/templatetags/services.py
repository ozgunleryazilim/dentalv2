from django import template
from page.models import ServiceCategory, ServicesPageSeo, ServiceItem

register = template.Library()


@register.simple_tag
def get_service_category_seo_obj():
    return ServicesPageSeo.objects.first()


@register.simple_tag
def get_service_category_list():
    return ServiceCategory.objects.all()


@register.simple_tag
def get_service_category_home_list():
    return ServiceCategory.objects.filter(in_home=True)[:3]


@register.simple_tag
def get_service_item_list(limit=None):
    query = ServiceItem.objects.all()
    if limit:
        return query[:limit]
    return query


@register.simple_tag
def get_service_item_home_list(limit=None):
    return ServiceItem.objects.filter(in_home=True)[:3]

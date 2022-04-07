from django import template
from page.models import BlogCategory, BlogsPageSeo, Blog

register = template.Library()


@register.simple_tag
def get_blog_category_seo_obj():
    return BlogsPageSeo.objects.first()


@register.simple_tag
def get_blog_category_list():
    return BlogCategory.objects.all()


@register.simple_tag
def get_blog_home_list():
    return Blog.objects.all()[:3]


@register.simple_tag
def get_popular_blogs():
    return Blog.objects.order_by('-view_count')[:3]

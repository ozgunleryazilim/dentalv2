from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from page.models import ServiceItem, Blog
from utils.sitemaps import ModelSitemap


class PageStaticViewSitemap(Sitemap):
    i18n = True
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ['home', 'about', 'services', 'how_it_works', 'before_after', 'blog_list', 'contact',
                'appointment', 'gdpr']

    def location(self, item):
        return reverse(item)


class ServicesViewSitemap(ModelSitemap):
    model = ServiceItem
    changefreq = "daily"
    priority = 0.7


class BlogViewSitemap(ModelSitemap):
    model = Blog
    changefreq = "daily"
    priority = 0.7

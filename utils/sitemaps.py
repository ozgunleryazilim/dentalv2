from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.utils.translation import activate


class ModelSitemap(Sitemap):
    i18n = True
    queryset = None
    model = None

    def items(self):
        i18n_objects = []
        for lang_code, lang in settings.LANGUAGES:
            activate(lang_code)
            for obj in self.queryset or self.model.objects.all():
                i18n_objects.append(obj.get_absolute_url())
        return i18n_objects

    def location(self, obj):
        return obj

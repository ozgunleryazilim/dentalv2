from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin
from page.models import (Keywords, HomeSlider, seo_translations, HomePageSeo)

admin.site.register(Keywords, TranslatableAdmin)

seo_fields = tuple(seo_translations.keys()) + ("meta_keywords",)


@admin.register(HomeSlider)
class HomeSliderAdmin(TranslatableAdmin):
    search_fields = ('title',)
    list_display = ('title', 'redirect_url',)
    fields = ('title', 'description', 'redirect_url', 'image')


@admin.register(HomePageSeo)
class HomePageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Seo Bilgileri"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)

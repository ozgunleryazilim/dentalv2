from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin
from page.models import (Keywords, HomeSlider, seo_translations, HomePageSeo, ServiceCategory)

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


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Category Information"), {'fields': ('name', 'description', 'icon', 'in_home')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('name', 'icon', 'in_home')
    list_editable = ('icon', 'in_home')
    list_filter = ('icon', 'in_home')
    search_fields = ('name',)

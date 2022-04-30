from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from page.models import (Keywords, HomeSlider, seo_translations, HomePageSeo, ServiceCategory, ServiceItem,
                         ServicesPageSeo, BeforeAfterImage, AboutPageSeo, FrequentlyAskedQuestion, HowItWorksPageSeo,
                         BeforeAfterPageSeo, BlogsPageSeo, BlogCategory, Blog, BlogComment, ContactPageSeo,
                         AppointmentPageSeo, GDPRPageSeo)

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
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


@admin.register(ServicesPageSeo)
class ServicesPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Category Information"), {'fields': ('name', 'slug', 'description', 'icon', 'in_home')}),
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('name', 'icon', 'in_home')
    list_editable = ('icon', 'in_home')
    list_filter = ('icon', 'in_home')
    search_fields = ('name',)

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',),
        }


@admin.register(ServiceItem)
class ServiceItemAdmin(TranslatableAdmin):
    fieldsets = (
        (None, {'fields': ('banner_title', 'slug', 'category', 'banner_description', 'home_description',
                           'content', 'image', 'banner_image', 'icon','in_home')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('banner_title', 'slug', 'category', 'icon', 'in_home')
    list_editable = ('icon', 'in_home')
    list_filter = ('category', 'icon', 'in_home')
    search_fields = ('banner_title',)

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('banner_title',)
        }


@admin.register(BeforeAfterImage)
class BeforeAfterImageAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutPageSeo)
class AboutPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Content 1"), {'fields': ('content_title1', 'content_body1', 'content_image1')}),
        (_("Content 2"), {'fields': ('content_title2', 'content_body2', 'content_image2')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('banner_title',)


@admin.register(HowItWorksPageSeo)
class HowItWorksPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('banner_title',)


@admin.register(BeforeAfterPageSeo)
class BeforeAfterPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('banner_title',)


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(TranslatableAdmin):
    fields = ('question', 'answer', 'service')
    list_display = ('question',)


@admin.register(BlogsPageSeo)
class BlogsPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


@admin.register(BlogCategory)
class BlogCategoryAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Category Information"), {'fields': ('title', 'slug', 'description', 'image', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('title', 'slug')
    search_fields = ('title',)

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',),
        }


class BlogCommentInline(admin.StackedInline):
    model = BlogComment


@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Blog Information"),
         {'fields': ('title', 'slug', 'category', 'description', 'content', 'image', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    inlines = (BlogCommentInline,)
    filter_vertical = ('meta_keywords',)
    list_display = ('title', 'slug', 'category')
    list_filter = ('category',)
    search_fields = ('title',)

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'is_approved')
    list_filter = ('is_approved',)
    list_editable = ('is_approved',)
    search_fields = ('name',)


@admin.register(ContactPageSeo)
class ContactPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('banner_title',)


@admin.register(AppointmentPageSeo)
class AppointmentPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('banner_title',)


@admin.register(GDPRPageSeo)
class GDPRPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Content Information"), {'fields': ('content',)}),
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("SEO Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('banner_title',)

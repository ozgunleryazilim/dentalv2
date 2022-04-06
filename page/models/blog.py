from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel
from utils.models import TimestampStarterModel


class BlogsPageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(
        banner_title=models.CharField(_("Title"), max_length=200, blank=True, null=True),
        banner_description=models.TextField(_("Description"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(_("Banner Image"), upload_to="blogs/banner", blank=True, null=True)

    class Meta:
        verbose_name = _("Blogs Page SEO")
        verbose_name_plural = _("Blogs Page SEO")


class BlogCategory(TranslatableModel, SEOStarterModel, TimestampStarterModel):
    translations = TranslatedFields(
        title=models.CharField(_("Category Name"), max_length=200),
        slug=models.SlugField(_("Slug"), max_length=200),
        description=models.TextField(_("Description"), blank=True, null=True),
        **seo_translations
    )
    image = models.ImageField(_("Image"), upload_to="blogs", blank=True, null=True)
    banner_image = models.ImageField(_("Banner Image"), upload_to="blogs/banner", blank=True, null=True)

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")

    def __str__(self):
        return self.title


class Blog(TranslatableModel, SEOStarterModel, TimestampStarterModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200),
        description=models.TextField(_("Description"), blank=True, null=True),
        slug=models.SlugField(_("Slug"), max_length=200),
        content=RichTextUploadingField(_("Content Body 1"), blank=True, null=True),
        **seo_translations
    )
    category = models.ForeignKey(BlogCategory, blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name=_("Kategori"))
    banner_image = models.ImageField(_("Banner Image"), upload_to="services/banner", blank=True, null=True)
    image = models.ImageField(_("Service Image"), upload_to="services", blank=True, null=True)
    view_count = models.IntegerField(default=0, verbose_name=_("View Count"))

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blog")

    def __str__(self):
        return self.title

    def increase_view_count(self):
        self.view_count += 1
        self.save()


class BlogComment(TimestampStarterModel):
    blog = models.ForeignKey(Blog, verbose_name=_("Blog"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_("Name *"), max_length=200)
    email = models.EmailField(verbose_name=_("Email *"))
    comment = models.TextField(verbose_name=_("Write review *"))
    is_approved = models.BooleanField(verbose_name=_("Is Approved"), default=False)

    class Meta:
        verbose_name = _("Blog Comment")
        verbose_name_plural = _("Blog Comments")
        ordering = ('-created_date',)

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel


class AboutPageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(
        banner_title=models.CharField(_("Banner Title"), max_length=200),
        banner_description=models.TextField(_("Banner Description"), blank=True, null=True),

        content_title1=models.CharField(_("Content Title 1"), max_length=200, blank=True, null=True),
        content_body1=RichTextUploadingField(_("Content Body 1"), blank=True, null=True),

        content_title2=models.CharField(_("Content Title 2"), max_length=200, blank=True, null=True),
        content_body2=RichTextUploadingField(_("Content Body 2"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(_("Banner Image"), upload_to="about/banner", blank=True, null=True)
    content_image1 = models.ImageField(_("Content Image 1"), upload_to="about", blank=True, null=True)
    content_image2 = models.ImageField(_("Content Image 2"), upload_to="about", blank=True, null=True)

    class Meta:
        verbose_name = _("About Page SEO")
        verbose_name_plural = _("About Page SEO")

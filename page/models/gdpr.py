from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor_uploader.fields import RichTextUploadingField

from page.models import seo_translations, SEOStarterModel


class GDPRPageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(
        banner_title=models.CharField(_("Banner Title"), max_length=200),
        banner_description=models.TextField(_("Banner Description"), blank=True, null=True),
        content=RichTextUploadingField(verbose_name=_("Content"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(_("Banner Image"), upload_to="about/banner", blank=True, null=True)

    class Meta:
        verbose_name = _("GDPR Page SEO")
        verbose_name_plural = _("GDPR Page SEO")

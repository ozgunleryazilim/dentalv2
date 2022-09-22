from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel
from popup.models import Popup


class AppointmentPageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(
        banner_title=models.CharField(_("Banner Title"), max_length=200),
        banner_description=models.TextField(
            _("Banner Description"), blank=True, null=True
        ),
        **seo_translations
    )
    banner_image = models.ImageField(
        _("Banner Image"), upload_to="about/banner", blank=True, null=True
    )
    popup = models.ForeignKey(
        Popup, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Popup")
    )

    class Meta:
        verbose_name = _("Appointment Page SEO")
        verbose_name_plural = _("Appointment Page SEO")

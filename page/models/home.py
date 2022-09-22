from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel
from utils.models import TimestampStarterModel
from popup.models import Popup


class HomePageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(**seo_translations)
    popup = models.ForeignKey(
        Popup, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Popup")
    )

    class Meta:
        verbose_name = _("Home Page SEO")
        verbose_name_plural = _("Home Page SEO")


class HomeSlider(TranslatableModel, TimestampStarterModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200),
        description=models.TextField(_("Description"), blank=True, null=True),
        redirect_url=models.CharField(
            _("Redirect URL"), max_length=200, blank=True, null=True
        ),
    )
    image = models.ImageField(
        verbose_name=_("Image"), upload_to="homeslider", blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Home Slider")
        verbose_name_plural = _("Home Sliders")

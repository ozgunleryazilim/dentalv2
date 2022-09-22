from tabnanny import verbose
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import ugettext_lazy as _


class PopupService(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(verbose_name=_("Title"), max_length=200)
    )

    class Meta:
        verbose_name = _("Popup Service")
        verbose_name_plural = _("Popup Services")

    def __str__(self):
        return self.title


class Popup(TranslatableModel):
    name = models.CharField(max_length=100, verbose_name=_("Popup Name"))
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_("Title")),
        subtitle=models.TextField(blank=True, null=True, verbose_name=_("Subtitle")),
    )
    image = models.ImageField(
        upload_to="popup", blank=True, null=True, verbose_name=_("Popup Image")
    )
    services = models.ManyToManyField(
        PopupService, blank=True, verbose_name=_("Services")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active?"))

    class Meta:
        verbose_name = _("Popup")
        verbose_name_plural = _("Popups")

    def __str__(self) -> str:
        return self.name

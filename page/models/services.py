from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel
from utils.models import TimestampStarterModel


class ServiceCategory(TranslatableModel, SEOStarterModel, TimestampStarterModel):
    class ServiceCategoryIcons(models.Choices):
        MICROSCOPE = "fa-microscope"
        TEETH = "fa-teeth"
        BONE_BREAK = "fa-bone-break"
        SCALPEL_PATH = "fa-scalpel-path"
        HEAD_SIDE_BRAIN = "fa-head-side-brain"
        HEARTH_RATE = "fa-heart-rate"

    translations = TranslatedFields(
        name=models.CharField(_("Category Name"), max_length=200),
        description=models.TextField(_("Description"), blank=True, null=True),
        **seo_translations
    )
    icon = models.CharField(_("Category Icon"), max_length=50,
                            choices=ServiceCategoryIcons.choices, blank=True, null=True)
    in_home = models.BooleanField(_("In home page services section?"), default=False)

    class Meta:
        verbose_name = _("Service Category")
        verbose_name_plural = _("Service Categories")

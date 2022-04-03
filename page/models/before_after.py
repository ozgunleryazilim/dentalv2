from django.db import models
from django.utils.translation import ugettext_lazy as _


class BeforeAfterImage(models.Model):
    name = models.CharField(_("Name"), max_length=50,
                            blank=True, null=True, default="")
    image = models.ImageField(_("Image"), upload_to="before_after")

    class Meta:
        verbose_name = _("Before & After Image")
        verbose_name_plural = _("Before & After Images")

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from page.models import ServiceItem

class FrequentlyAskedQuestion(TranslatableModel):
    translations = TranslatedFields(
        question=models.CharField(_("Question"), max_length=200),
        answer=RichTextField(_("Answer"), blank=True, null=True),
    )
    service = models.ForeignKey(ServiceItem, verbose_name=_("Related Service"), blank=True, null=True,
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Frequently Asked Question")
        verbose_name_plural = _("Frequently Asked Questions")

    def __str__(self):
        return self.question

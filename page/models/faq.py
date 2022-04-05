from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class FrequentlyAskedQuestion(TranslatableModel):
    translations = TranslatedFields(
        question=models.CharField(_("Question"), max_length=200),
        answer=RichTextField(_("Answer"), blank=True, null=True),
    )

    class Meta:
        verbose_name = _("Frequently Answered Question")
        verbose_name_plural = _("Frequently Answered Questions")

    def __str__(self):
        return self.question

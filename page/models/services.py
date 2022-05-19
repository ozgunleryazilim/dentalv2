from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import switch_language

from page.models import seo_translations, SEOStarterModel
from utils.models import TimestampStarterModel


class ServicesPageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(
        banner_title=models.CharField(_("Title"), max_length=200, blank=True, null=True),
        banner_description=RichTextField(_("Description"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(_("Banner Image"), upload_to="services/banner", blank=True, null=True)

    class Meta:
        verbose_name = _("Service Page SEO")
        verbose_name_plural = _("Service Page SEO")


class ServiceCategory(TranslatableModel, SEOStarterModel, TimestampStarterModel):
    class ServiceCategoryIcons(models.Choices):
        MICROSCOPE = "fa-microscope"
        TEETH = "fa-teeth"
        BONE_BREAK = "fa-bone-break"
        SCALPEL_PATH = "fa-scalpel-path"
        HEAD_SIDE_BRAIN = "fa-head-side-brain"
        HEARTH_RATE = "fa-heart-rate"
        CAGRI_MERKEZI = "cagri-merkezi.svg"
        DENTAL_1 = "dental-1.svg"
        DIS_KORUMA = "dis-koruma.svg"
        DIS_MUAYENE = "dis-muayene.svg"
        HOLLYWOOD_SMILE = "hollywood-smile.svg"
        IMPLANT_TEDAVISI = "implant-tedavisi.svg"
        ORTHODONTI = "orthodonti.svg"
        ORTHODONTI_2 = "orthodonti-2.svg"
        TEETH_1 = "teeth-1.svg"
        TEETH_2 = "teeth-2.svg"
        TEETH_3 = "teeth-3.svg"
        TEETH_4 = "teeth-4.svg"
        TEETH_5 = "teeth-5.svg"
        TEETH_6 = "teeth-6.svg"
        TOMOGRAFI = "tomografi.svg"

    translations = TranslatedFields(
        name=models.CharField(_("Category Name"), max_length=200),
        slug=models.SlugField(_("Slug"), max_length=200),
        description=models.TextField(_("Description"), blank=True, null=True),
        banner_title=models.CharField(_("Title"), max_length=200, blank=True, null=True),
        banner_description=RichTextField(_("Description"), blank=True, null=True),
        **seo_translations
    )
    icon = models.CharField(_("Category Icon"), max_length=50,
                            choices=ServiceCategoryIcons.choices, blank=True, null=True)
    in_home = models.BooleanField(_("In home page services section?"), default=False)
    banner_image = models.ImageField(_("Banner Image"), upload_to="services/banner", blank=True, null=True)

    class Meta:
        verbose_name = _("Service Category")
        verbose_name_plural = _("Service Categories")

    def __str__(self):
        return self.name


class ServiceItem(TranslatableModel, SEOStarterModel, TimestampStarterModel):
    class ServiceIcons(models.Choices):
        MICROSCOPE = "fa-microscope"
        TEETH = "fa-teeth"
        BONE_BREAK = "fa-bone-break"
        SCALPEL_PATH = "fa-scalpel-path"
        HEAD_SIDE_BRAIN = "fa-head-side-brain"
        HEARTH_RATE = "fa-heart-rate"
        CAGRI_MERKEZI = "cagri-merkezi.svg"
        DENTAL_1 = "dental-1.svg"
        DIS_KORUMA = "dis-koruma.svg"
        DIS_MUAYENE = "dis-muayene.svg"
        HOLLYWOOD_SMILE = "hollywood-smile.svg"
        IMPLANT_TEDAVISI = "implant-tedavisi.svg"
        ORTHODONTI = "orthodonti.svg"
        ORTHODONTI_2 = "orthodonti-2.svg"
        TEETH_1 = "teeth-1.svg"
        TEETH_2 = "teeth-2.svg"
        TEETH_3 = "teeth-3.svg"
        TEETH_4 = "teeth-4.svg"
        TEETH_5 = "teeth-5.svg"
        TEETH_6 = "teeth-6.svg"
        TOMOGRAFI = "tomografi.svg"
    translations = TranslatedFields(
        banner_title=models.CharField(_("Title"), max_length=200),
        banner_description=RichTextField(_("Banner Description"), blank=True, null=True),
        home_description=RichTextField(_("Home Description"), blank=True, null=True),
        slug=models.SlugField(_("Slug"), max_length=200),
        content=RichTextUploadingField(_("Content Body"), blank=True, null=True),
        **seo_translations
    )
    category = models.ForeignKey(ServiceCategory, blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name=_("Kategori"))
    icon = models.CharField(_("Category Icon"), max_length=50, choices=ServiceIcons.choices, blank=True, null=True)
    banner_image = models.ImageField(_("Banner Image"), upload_to="services/banner", blank=True, null=True)
    image = models.ImageField(_("Service Image"), upload_to="services", blank=True, null=True)
    in_home = models.BooleanField(_("In home page services section?"), default=False)

    class Meta:
        verbose_name = _("Service Item")
        verbose_name_plural = _("Service Items")

    def __str__(self):
        return self.banner_title

    def get_absolute_url(self):
        with switch_language(self):
            return reverse('services_detail', args=(self.slug,))
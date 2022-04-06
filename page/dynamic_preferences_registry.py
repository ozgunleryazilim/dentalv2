from django.utils.translation import ugettext_lazy as _
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.types import StringPreference

SECTION_NAME = 'page'
page = Section(SECTION_NAME)

saved_preferences = global_preferences_registry.manager()


@global_preferences_registry.register
class PhoneNumber(StringPreference):
    section = page
    name = 'phone_number'
    default = "+90 555 156 05 05"
    verbose_name = _("Phone Number")


@global_preferences_registry.register
class EmailAddress(StringPreference):
    section = page
    name = 'email_address'
    default = "info@dental-bosphorus.com"
    verbose_name = _("Email Address")


@global_preferences_registry.register
class FacebookLink(StringPreference):
    section = page
    name = 'facebook_link'
    default = ""
    verbose_name = _("Facebook Link")


@global_preferences_registry.register
class InstagramLink(StringPreference):
    section = page
    name = 'instagram_link'
    default = ""
    verbose_name = _("İnstagram Link")


@global_preferences_registry.register
class YoutubeLink(StringPreference):
    section = page
    name = 'youtube_link'
    default = ""
    verbose_name = _("Youtube Link")


@global_preferences_registry.register
class AddressLine1(StringPreference):
    section = page
    name = 'address_line1'
    default = "Adres Line 1"
    verbose_name = _("Adres Line 1")


@global_preferences_registry.register
class AddressLine2(StringPreference):
    section = page
    name = 'address_line2'
    default = "Adres Line 2"
    verbose_name = _("Adres Line 2")


@global_preferences_registry.register
class AddressLine3(StringPreference):
    section = page
    name = 'address_line3'
    default = "Adres Line 3"
    verbose_name = _("Adres Line 3")

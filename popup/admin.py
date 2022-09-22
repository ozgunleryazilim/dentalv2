from django.contrib import admin
from parler.admin import TranslatableAdmin
from popup.models import PopupService, Popup


@admin.register(PopupService)
class PopupServiceAdmin(TranslatableAdmin):
    fields = ("title",)
    list_display = ("title",)


@admin.register(Popup)
class PopupAdmin(TranslatableAdmin):
    fields = ("name", "title", "subtitle", "image", "services", "is_active")
    list_display = ("name", "title", "is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)

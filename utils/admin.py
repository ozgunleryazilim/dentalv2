from django.contrib import admin


class OneEntityModel(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return super().has_add_permission(request)


class HiddenModel(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

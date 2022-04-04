from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404


class DetailListView(SingleObjectMixin, ListView):
    detail_object_name = "object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self.model.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queries_without_page = self.request.GET.copy()
        if queries_without_page.get("page"):
            del queries_without_page["page"]
        context['queries'] = queries_without_page
        context[self.detail_object_name] = self.object

        return context

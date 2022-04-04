from django.views.generic import TemplateView, ListView, DetailView
from parler.views import TranslatableSlugMixin

from page.models import ServiceItem, ServiceCategory


class HomePage(TemplateView):
    template_name = "page/home.html"


class AboutPage(TemplateView):
    template_name = "page/about.html"


class ServicesPage(ListView):
    template_name = "page/services.html"
    model = ServiceItem
    paginate_by = 9
    context_object_name = "services"
    category = None

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.request.GET.get('category')
        if not slug:
            return queryset
        try:
            self.category = ServiceCategory.objects.active_translations(slug=slug).get()
            return queryset.filter(category=self.category)
        except ServiceCategory.DoesNotExist:
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queries_without_page = self.request.GET.copy()
        if queries_without_page.get("page"):
            del queries_without_page["page"]
        context['queries'] = queries_without_page
        context['category'] = self.category
        return context


class ServicesDetailPage(TranslatableSlugMixin, DetailView):
    template_name = "page/services-detail.html"
    model = ServiceItem
    context_object_name = "service"


class HowItWorksPage(TemplateView):
    template_name = "page/how-it-works.html"

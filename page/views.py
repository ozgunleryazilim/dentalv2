from django.views.generic import TemplateView, ListView, DetailView
from parler.views import TranslatableSlugMixin

from page.models import ServiceItem, ServiceCategory, BeforeAfterImage, BlogCategory, Blog
from utils.views import CategoriedListView


class HomePage(TemplateView):
    template_name = "page/home.html"


class AboutPage(TemplateView):
    template_name = "page/about.html"


class ServicesPage(CategoriedListView):
    template_name = "page/services.html"
    model = ServiceItem
    paginate_by = 9
    context_object_name = "services"
    category = None
    category_model = ServiceCategory


class ServicesDetailPage(TranslatableSlugMixin, DetailView):
    template_name = "page/services-detail.html"
    model = ServiceItem
    context_object_name = "service"


class HowItWorksPage(TemplateView):
    template_name = "page/how-it-works.html"


class BeforeAfterPage(ListView):
    template_name = "page/before_after.html"
    model = BeforeAfterImage
    paginate_by = 18
    context_object_name = "image_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queries_without_page = self.request.GET.copy()
        if queries_without_page.get("page"):
            del queries_without_page["page"]
        context['queries'] = queries_without_page
        return context


class BlogListPage(CategoriedListView):
    template_name = "page/blog-list.html"
    model = Blog
    paginate_by = 9
    context_object_name = "blog_list"
    category = None
    category_model = BlogCategory

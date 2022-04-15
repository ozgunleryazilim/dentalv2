from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from parler.views import TranslatableSlugMixin

from page.forms import BlogCommentForm
from page.models import ServiceItem, ServiceCategory, BeforeAfterImage, BlogCategory, Blog
from utils.views import CategoriedListView, DetailListView


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faq_list'] = self.object.frequentlyaskedquestion_set.all()
        return context


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


class BlogDetailPage(TranslatableSlugMixin, FormMixin, DetailListView):
    model = Blog
    template_name = "page/blog-detail.html"
    detail_object_name = "blog"
    paginate_by = 10
    form_class = BlogCommentForm

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increase_view_count()
        return response

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'slug': self.object.slug})

    def get_queryset(self):
        return self.object.blogcomment_set.filter(is_approved=True).order_by('-created_date')

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.blog = self.object
        comment.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self.model.objects.all())
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)


class ContactPage(TemplateView):
    template_name = "page/contact.html"


class AppointmentPage(TemplateView):
    template_name = "page/appointment.html"


class GDPRPage(TemplateView):
    template_name = "page/gdpr.html"

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import get_language
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from parler.utils.context import switch_language
from parler.views import TranslatableSlugMixin, ViewUrlMixin

from page.forms import BlogCommentForm
from page.models import (
    ServiceItem,
    ServiceCategory,
    BeforeAfterImage,
    BlogCategory,
    Blog,
)
from utils.recaptcha import validate_recaptcha, RecaptchaValidationError
from utils.views import CategoriedListView, DetailListView, HandleEmailFormView


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


class ServicesDetailPage(TranslatableSlugMixin, ViewUrlMixin, DetailView):
    template_name = "page/services-detail.html"
    model = ServiceItem
    context_object_name = "service"
    view_url_name = "services_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["faq_list"] = self.object.frequentlyaskedquestion_set.all()
        return context

    def get_view_url(self):
        with switch_language(self.object, get_language()):
            return reverse(self.view_url_name, kwargs={"slug": self.object.slug})


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
        context["queries"] = queries_without_page
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
    form_identifier = "comment-form"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increase_view_count()
        return response

    def get_success_url(self):
        return reverse("blog_detail", kwargs={"slug": self.object.slug})

    def get_queryset(self):
        return self.object.blogcomment_set.filter(is_approved=True).order_by(
            "-created_date"
        )

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.blog = self.object
        comment.save()
        return super().form_valid(form)

    def recaptcha_invalid(self, request):
        return redirect(
            "{}#{}".format(request.META["HTTP_REFERER"], self.form_identifier)
        )

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self.model.objects.all())

        try:
            validate_recaptcha(request.POST)
        except RecaptchaValidationError as exc:
            messages.error(request, str(exc))
            return self.recaptcha_invalid(request)
        except Exception as e:
            print(e)
            messages.error(request, _("Mesajınız gönderilirken hata oluştu!"))
            return self.recaptcha_invalid(request)

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


class HomePageEmailFormView(HandleEmailFormView):
    subject = "DentalBosphorus - Anasayfa iletişim formu dolduruldu"
    email_template_name = "emailtemps/home_contact_form.html"

    def get_email_context(self, request):
        return {
            "full_name": request.POST.get("full_name", ""),
            "email": request.POST.get("email", ""),
            "treatment": request.POST.get("treatment_selection", ""),
            "phone": request.POST.get("contact-full_number", ""),
            "full_phone_number": request.POST.get("contact-full_number", ""),
            "message": request.POST.get("message", ""),
        }


class ServicesPageEmailFormView(HandleEmailFormView):
    subject = "DentalBosphorus - Servisler iletişim formu dolduruldu"
    email_template_name = "emailtemps/services_contact_form.html"
    form_identifier = "services-form"

    def get_email_context(self, request):
        return {
            "full_name": request.POST.get("full_name", ""),
            "email": request.POST.get("email", ""),
            "treatment": request.POST.get("treatment", ""),
            "phone": request.POST.get("phone", ""),
            "full_phone_number": request.POST.get("contact-full_number", ""),
            "message": request.POST.get("message", ""),
        }


class ServicesSideFormEmailView(HandleEmailFormView):
    subject = "DentalBosphorus - Servisler Yan iletişim formu dolduruldu"
    email_template_name = "emailtemps/services_side_contact_form.html"
    form_identifier = "services-side-form"

    def get_email_context(self, request):
        return {
            "full_name": request.POST.get("full_name", ""),
            "email": request.POST.get("email", ""),
            "treatment": request.POST.get("treatment", ""),
            "phone": request.POST.get("phone", ""),
            "full_phone_number": request.POST.get("contact-full_number", ""),
        }


class BlogSideFormEmailView(HandleEmailFormView):
    subject = "DentalBosphorus - Blog Yan iletişim formu dolduruldu"
    email_template_name = "emailtemps/blogs_side_contact_form.html"
    form_identifier = "blogs-side-form"

    def get_email_context(self, request):
        return {
            "full_name": request.POST.get("full_name", ""),
            "email": request.POST.get("email", ""),
            "treatment": request.POST.get("treatment", ""),
            "phone": request.POST.get("phone", ""),
            "full_phone_number": request.POST.get("contact-full_number", ""),
        }


class ContactFormEmailView(HandleEmailFormView):
    subject = "DentalBosphorus - İletişim Sayfası formu dolduruldu"
    email_template_name = "emailtemps/contact_form.html"
    form_identifier = "contact-form"

    def get_email_context(self, request):
        return {
            "full_name": request.POST.get("full_name", ""),
            "email": request.POST.get("email", ""),
            "treatment": request.POST.get("treatment", ""),
            "phone": request.POST.get("phone", ""),
            "full_phone_number": request.POST.get("contact-full_number", ""),
            "message": request.POST.get("message", ""),
        }


class AppointmentFormEmailView(HandleEmailFormView):
    subject = "DentalBosphorus - Randevu Sayfası formu dolduruldu"
    email_template_name = "emailtemps/appointment_form.html"
    form_identifier = "appointment-form"

    def get_email_context(self, request):
        return {
            "first_name": request.POST.get("first_name", ""),
            "last_name": request.POST.get("last_name", ""),
            "email": request.POST.get("email", ""),
            "treatment": request.POST.get("treatment", ""),
            "phone": request.POST.get("phone", ""),
            "full_phone_number": request.POST.get("contact-full_number", ""),
            "appointment_type": request.POST.get("appointment_type", ""),
        }


class PopupFormEmailView(HandleEmailFormView):
    subject = "DentalBosphorus - {service} için Popup form dolduruldu: {name}"
    email_template_name = "emailtemps/popup_form.html"
    form_identifier = "ad-popup-form"

    def get_email_context(self, request):
        return {
            "name": request.POST.get("name", ""),
            "email": request.POST.get("email", ""),
            "full_phone_number": request.POST.get("contact-full_number", ""),
            "phone": request.POST.get("phone", ""),
            "service": request.POST.get("service", ""),
            "message": request.POST.get("message", ""),
        }

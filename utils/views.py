from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin


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


class CategoriedListView(ListView):
    paginate_by = 9
    category = None
    category_model = None

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.request.GET.get('category')
        if not slug:
            return queryset
        try:
            self.category = self.category_model.objects.active_translations(slug=slug).get()
            return queryset.filter(category=self.category)
        except self.category_model.DoesNotExist:
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queries_without_page = self.request.GET.copy()
        if queries_without_page.get("page"):
            del queries_without_page["page"]
        context['queries'] = queries_without_page
        context['category'] = self.category
        return context


class HandleEmailFormView(View):
    sender = settings.DEFAULT_FROM_EMAIL
    receivers = settings.CONTACT_FORM_RECEIVER
    email_template_name = None
    subject = ""
    form_identifier = ""

    def get_email_context(self, request):
        raise NotImplementedError()

    def get_email_template(self):
        if not self.email_template_name:
            raise NotImplementedError("Template name is not configured!")
        return get_template(self.email_template_name)

    def send_email(self, request):
        context = self.get_email_context(request)
        subject = self.subject.format(**context)
        template = self.get_email_template()
        content = template.render(context)

        msg = EmailMultiAlternatives(subject, content, self.sender, self.receivers)
        msg.attach_alternative(content, 'text/html')
        msg.send()

    def post(self, request):
        try:
            self.send_email(request)
        except Exception as e:
            print(e)
            messages.error(request, _("Mesajınız gönderilirken hata oluştu!"))
        else:
            messages.success(request, _("Mesajınız başarıyla gönderildi! Size en kısa sürede geri dönüş yapacağız"))
        return redirect("{}#{}".format(request.META['HTTP_REFERER'], self.form_identifier))

from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "page/home.html"


class AboutPage(TemplateView):
    template_name = "page/about.html"


class ServicesPage(TemplateView):
    template_name = "page/services.html"
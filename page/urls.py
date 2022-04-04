from django.urls import path
from django.utils.translation import ugettext_lazy as _

from page.views import (HomePage, AboutPage, ServicesPage, ServicesDetailPage, HowItWorksPage)

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path(_('about/'), AboutPage.as_view(), name="about"),
    path(_('services/'), ServicesPage.as_view(), name="services"),
    path(_('services/<slug>/'), ServicesDetailPage.as_view(), name="services_detail"),
    path(_('how-it-works/'), HowItWorksPage.as_view(), name="how_it_works"),
]

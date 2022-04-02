from django.urls import path
from django.utils.translation import ugettext_lazy as _

from page.views import (HomePage, AboutPage, ServicesPage)

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path(_('about/'), AboutPage.as_view(), name="about"),
    path(_('services/'), ServicesPage.as_view(), name="services"),
]

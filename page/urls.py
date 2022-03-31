from django.urls import path
from django.utils.translation import ugettext_lazy as _

from page.views import (HomePage)

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
]

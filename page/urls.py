from django.urls import path
from django.utils.translation import ugettext_lazy as _

from page.views import (
    HomePage,
    AboutPage,
    ServicesPage,
    ServicesDetailPage,
    HowItWorksPage,
    BeforeAfterPage,
    BlogListPage,
    BlogDetailPage,
    ContactPage,
    AppointmentPage,
    GDPRPage,
    HomePageEmailFormView,
    ServicesPageEmailFormView,
    ServicesSideFormEmailView,
    BlogSideFormEmailView,
    ContactFormEmailView,
    AppointmentFormEmailView,
    PopupFormEmailView,
)

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path(_("about/"), AboutPage.as_view(), name="about"),
    path(_("services/"), ServicesPage.as_view(), name="services"),
    path(_("services/<slug>/"), ServicesDetailPage.as_view(), name="services_detail"),
    path(_("how-it-works/"), HowItWorksPage.as_view(), name="how_it_works"),
    path(_("before-after/"), BeforeAfterPage.as_view(), name="before_after"),
    path(_("blog/"), BlogListPage.as_view(), name="blog_list"),
    path(_("blog/<slug>/"), BlogDetailPage.as_view(), name="blog_detail"),
    path(_("contact/"), ContactPage.as_view(), name="contact"),
    path(_("appointment/"), AppointmentPage.as_view(), name="appointment"),
    path(_("gdpr/"), GDPRPage.as_view(), name="gdpr"),
    path(
        "handle_homepage_form/",
        HomePageEmailFormView.as_view(),
        name="handle_homepage_form",
    ),
    path(
        "handle_services_form/",
        ServicesPageEmailFormView.as_view(),
        name="handle_services_form",
    ),
    path(
        "handle_services_side_form/",
        ServicesSideFormEmailView.as_view(),
        name="handle_services_side_form",
    ),
    path(
        "handle_blogs_side_form/",
        BlogSideFormEmailView.as_view(),
        name="handle_blogs_side_form",
    ),
    path(
        "handle_contact_form/",
        ContactFormEmailView.as_view(),
        name="handle_contact_form",
    ),
    path(
        "handle_appointment_form/",
        AppointmentFormEmailView.as_view(),
        name="handle_appointment_form",
    ),
    path("handle_popup_form/", PopupFormEmailView.as_view(), name="handle_popup_form"),
]

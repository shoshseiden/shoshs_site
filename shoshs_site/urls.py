from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin

from . import views

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^websites/$", views.WebsiteView.as_view(), name="websites"),
    url(r"^graphics/$", views.GraphicView.as_view(), name="graphics"),
]

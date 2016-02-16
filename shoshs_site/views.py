from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django import template
from django.template.loader import get_template
from django.template import RequestContext, loader
from django.views import generic

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Website, Graphic


class WebsiteView(ListView):
    template_name = "websites.html"
    context_object_name = "website_list"

    def queryset(self):
        return Website.objects.order_by("website_name")


class GraphicView(ListView):
    template_name = "graphics.html"
    context_object_name = "graphics_list"

    def queryset(self):
        return Graphic.objects.order_by("graphic_image_description")

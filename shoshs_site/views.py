from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django import template
from django.template.loader import get_template
from django.template import RequestContext, loader
from django.views import generic

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Website, Graphic


class WebsiteView(ListView):
    model = Website
    template_name = "websites.html"

    def queryset(self):
        return Graphic.objects.order_by(website_name)


class GraphicView(ListView):
    model = Graphic
    template_name = "graphics.html"

    def queryset(self):
        return Graphic.objects.order_by(graphic_image_description)

from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class TestView(TemplateView):
    template_name = '404.html'



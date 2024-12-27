from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView


class index_view(TemplateView):
    template_name='index.html'

class about_view(TemplateView):
    template_name = 'about.html'


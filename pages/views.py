from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def homePageView(request):
    return HttpResponse("Welcome to my website")


class HomePage(TemplateView):
    template_name = 'pages/home.html'


class AboutPage(TemplateView):
    template_name = 'pages/about.html'


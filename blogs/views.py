from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blogs.models import BlogsModel


class BlogsView(ListView):
    model = BlogsModel
    template_name = 'blogs_home.html'


class BlogsPost(ListView):
    model = BlogsModel
    template_name = 'blogs_post.html'
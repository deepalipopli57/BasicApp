from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blogs.models import BlogsModel


class BlogsView(ListView):
    model = BlogsModel
    template_name = 'blogs_home.html'


class BlogsPost(ListView):
    model = BlogsModel
    template_name = 'pages/blogs_post.html'
    context_object_name = 'anything_you_want'


class BlogsCreateView(ListView):
    model = BlogsModel
    template_name = 'pages/post_new.html'
    fields = '__all__'


class BlogsUpdate(ListView):
    model = BlogsModel
    template_name = 'pages/post_edit.html'
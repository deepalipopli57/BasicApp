from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from posts.models import PostModel


class PostView(ListView):
    model = PostModel
    template_name = 'home.html'
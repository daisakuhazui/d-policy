from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Post

class PostIndex(generic.ListView):
    model = Post
    template_name = 'blog/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

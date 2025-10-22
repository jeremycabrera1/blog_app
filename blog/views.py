from django.shortcuts import render, get_list_or_404
from django.urls import reverse_lazy

from django.views.generic import TemplateView

# Create your views here.

from .models import Category, Post, Comment

# class PostView(TemplateView):
#     model = Post
#     fields = "__all__"
#     template_name = 'blog/index.html'

def read_post(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/index.html', context)
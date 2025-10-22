from django.shortcuts import render, get_list_or_404
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView, CreateView

# Create your views here.

from .models import Category, Post, Comment

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'categories',]
    success_url = reverse_lazy('posts')
    def form_valid(self, form):
            form.instance.owner = self.request.user # Assuming 'owner' is the ForeignKey field
            return super().form_valid(form)

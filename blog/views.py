from django.shortcuts import render, get_list_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

from .models import Category, Post, Comment


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'categories',]
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'categories',]
    success_url = reverse_lazy('posts')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    template_name = 'blog/post_confirm_delete.html'

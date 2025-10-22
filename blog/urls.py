from django.contrib import admin
from django.urls import path, include

from .views import PostListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('create-post', PostCreateView.as_view(), name='create_post'),
]
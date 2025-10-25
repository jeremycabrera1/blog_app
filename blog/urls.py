from django.contrib import admin
from django.urls import path, include

from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('create-post/', PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/update-post/', PostUpdateView.as_view(), name='update_post'),
    path('<int:pk>/delete-post/', PostDeleteView.as_view(), name='delete_post'),
]
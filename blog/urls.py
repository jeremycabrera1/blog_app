from django.contrib import admin
from django.urls import path, include

from .views import read_post

urlpatterns = [
    #path('', PostView.as_view(), name='posts'),
    path('', read_post, name='posts'),
]
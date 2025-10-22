from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.category}"
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='posts')


    def __str__(self):
        return f"{self.title}"


class comment(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
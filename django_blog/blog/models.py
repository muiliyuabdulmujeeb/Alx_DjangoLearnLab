from django.db import models
from django.contrib.auth.models import User
from blog_auth.models import BlogUser

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    author= models.ForeignKey(BlogUser, on_delete= models.CASCADE)
    published_date= models.DateTimeField(auto_now_add=True)
    last_editted = models.DateTimeField(auto_now_add=True)
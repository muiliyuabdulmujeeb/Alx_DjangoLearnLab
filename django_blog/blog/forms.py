from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BlogUser, Post



class BlogUserCreationForm(UserCreationForm):
    class Meta:
        model= BlogUser
        fields= ["first_name", "last_name", "email", "username", "password1", "password2"]

class BlogUserUpdateForm(forms.ModelForm):
    class Meta:
        model= BlogUser
        fields= ["first_name", "last_name", "email", "username", "bio"]

class BlogPostCreateForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ["title", "content"]

class BlogPostUpdateForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ["title", "content"]
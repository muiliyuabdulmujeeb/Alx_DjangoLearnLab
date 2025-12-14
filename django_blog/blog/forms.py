from django import forms
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagField, TagWidget
from .models import BlogUser, Post, Comment



class BlogUserCreationForm(UserCreationForm):
    class Meta:
        model= BlogUser
        fields= ["first_name", "last_name", "email", "username", "password1", "password2"]

class BlogUserUpdateForm(forms.ModelForm):
    class Meta:
        model= BlogUser
        fields= ["first_name", "last_name", "email", "username", "bio"]

class BlogPostCreateForm(forms.ModelForm):
    tags = TagField(required=None, widget=TagWidget())
    class Meta:
        model= Post
        fields= ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"rows": 5}),
        }

class BlogPostUpdateForm(forms.ModelForm):
    tags = TagField(required=None, widget=TagWidget())
    class Meta:
        model= Post
        fields= ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"rows": 5}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
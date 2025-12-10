from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import BlogUser



class BlogUserCreationForm(UserCreationForm):
    class Meta:
        model= BlogUser
        fields= ["first_name", "last_name", "email", "username", "password1", "password2"]

class BlogUserUpdateForm(ModelForm):
    class Meta:
        model= BlogUser
        fields= ["first_name", "last_name", "email", "username", "bio"]
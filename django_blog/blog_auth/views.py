from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .models import BlogUser
from .forms import BlogUserCreationForm

# Create your views here.

def create_user(request):
    if request.method == "POST":
        form = BlogUserCreationForm(data= request.POST)
        if form.is_valid:
            login(request, form.save())
            return redirect("posts")
    else:
        form = BlogUserCreationForm()
    
    return render(request, "blog_auth/registration.html", context={"form": form})

def user_profile(request):
    user = get_object_or_404(BlogUser, id= request.user)
    return render(request, "blog_auth/profile.html", {"user": user})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from blog_auth.models import BlogUser
from .forms import BlogUserCreationForm, BlogUserUpdateForm

# Create your views here.

def create_user(request):
    if request.method == "POST":
        form = BlogUserCreationForm(data= request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts")
    else:
        form = BlogUserCreationForm()
    
    return render(request, "blog/registration.html", context={"form": form})

@login_required(login_url="login")
def user_profile(request):
    if request.method == "POST":
        user = BlogUser.objects.get(id=request.user.pk)
        form = BlogUserUpdateForm(data= request.POST, instance= user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        user = BlogUser.objects.get(id=request.user.pk)
        form = BlogUserUpdateForm()
        return render(request, "blog/profile.html", {"user": user, "form": form})
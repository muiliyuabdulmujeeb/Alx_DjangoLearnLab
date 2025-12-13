from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog_auth.models import BlogUser
from .models import Post
from .forms import BlogUserCreationForm, BlogUserUpdateForm, BlogPostCreateForm, BlogPostUpdateForm

# Create your views here.

def create_user(request):
    """function based view to create a new user"""
    if request.method == "POST":
        form = BlogUserCreationForm(data= request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("blogposts")
    else:
        form = BlogUserCreationForm()
    
    return render(request, "blog/register.html", context={"form": form})

@login_required(login_url="login")
def user_profile(request):
    """Function based view to get user profile"""
    if request.method == "POST":
        user = BlogUser.objects.get(id=request.user.pk)
        form = BlogUserUpdateForm(request.POST, instance= user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        user = BlogUser.objects.get(id=request.user.pk)
        form = BlogUserUpdateForm(instance= user)
        return render(request, "blog/profile.html", {"user": user, "form": form})
    
def home(request):
    """A simple homepage for the website"""
    return render(request, 'blog/home.html')


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    """Class based view for creating a blogpost. A user must be signed in to be able to create a blogpost"""

    login_url=reverse_lazy("login")
    template_name= "blog/createblog.html"
    model= Post
    form_class = BlogPostCreateForm
    success_url = reverse_lazy("blogposts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogPostListView(LoginRequiredMixin, ListView):
    """Class based view for listing all blogposts, A user has to be signed in to be able to view them"""

    login_url=reverse_lazy("login")
    template_name= "blog/listblog.html"
    context_object_name= "blogposts"
    queryset= Post.objects.all()

class BlogPostDetailView(LoginRequiredMixin, DetailView):
    """Class based view for the detail of a specific blogpost, A user has to be signed in to be able to view them"""

    login_url=reverse_lazy("login")
    template_name= "blog/detailblog.html"
    context_object_name = "blogpost"
    queryset= Post.objects.all()

class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Class based view for updating a blogpost, A user has to be signed in and be its author to be able to edit them"""

    login_url=reverse_lazy("login")
    template_name= "blog/updateblog.html"
    context_object_name= "blogpost"
    model= Post
    form_class= BlogPostUpdateForm
    success_url= reverse_lazy("blogposts")

    def test_func(self):
        pk= self.kwargs.get("pk")
        post = Post.objects.get(pk= pk)
        return self.request.user == post.author
    

class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Class based view for deleting a blogpost, A user has to be signed in and be its author to be able to delete them"""

    login_url= reverse_lazy("login")
    model= Post
    success_url= reverse_lazy("home")

    def test_func(self):
        pk= self.kwargs.get("pk")
        post = Post.objects.get(pk= pk)
        return self.request.user == post.author

from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog_auth.models import BlogUser
from .models import Post, Comment
from .forms import BlogUserCreationForm, BlogUserUpdateForm, BlogPostCreateForm, BlogPostUpdateForm, CommentForm

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
    template_name= "blog/post_create.html"
    model= Post
    form_class = BlogPostCreateForm
    success_url = reverse_lazy("blogposts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogPostListView(LoginRequiredMixin, ListView):
    """Class based view for listing all blogposts, A user has to be signed in to be able to view them"""

    login_url=reverse_lazy("login")
    template_name= "blog/post_list.html"
    context_object_name= "blogposts"
    queryset= Post.objects.all()

class BlogPostDetailView(LoginRequiredMixin, DetailView):
    """Class based view for the detail of a specific blogpost, A user has to be signed in to be able to view them"""

    login_url=reverse_lazy("login")
    template_name= "blog/post_detail.html"
    context_object_name = "blogpost"
    queryset= Post.objects.all()

class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Class based view for updating a blogpost, A user has to be signed in and be its author to be able to edit them"""

    login_url=reverse_lazy("login")
    template_name= "blog/post_update.html"
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


class CommentListView(LoginRequiredMixin, ListView):
    """Class based view for listing all blogpost comments, A user has to be signed in to be able to view them"""

    login_url=reverse_lazy("login")
    template_name= "blog/post_detail.html"
    context_object_name= "blogpost_comments"
    
    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return super().get_queryset(Comment.objects.filter(post= post_id))
    
class CommentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    login_url= reverse_lazy("login")
    template_name= "blog/post_detail.html"
    context_object_name= "blogpost_comment"
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    """Class based view for creating a blogpost comment. A user must be signed in to be able to create a comment"""

    login_url=reverse_lazy("login")
    template_name= "blog/post_detail.html"
    model= Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.kwargs.get("post_id")
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detail_blogpost', kwargs={"pk": self.kwargs.get("post_id")})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = reverse_lazy("login")
    template_name = "blog/post_detail.html"
    form_class = CommentForm
    model= Comment
    
    def test_func(self):
        comment_id = self.kwargs["comment_id"]
        comment = Comment.objects.get(pk= comment_id)
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy("detail_blogpost", kwargs= {"pk": self.kwargs.get("post_id")})
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url= reverse_lazy("login")
    model= Comment

    def test_func(self):
        comment_id = self.kwargs["comment_id"]
        comment = Comment.objects.get(pk= comment_id)
        return self.request.user == comment.author
    
    def get_success_url(self):
        return reverse("detail_blogpost", kwargs={"pk": self.kwargs["post_id"]})
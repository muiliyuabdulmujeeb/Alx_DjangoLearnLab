from django.shortcuts import render, redirect
from django.forms import  modelform_factory
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
from .models import Book
from .models import Library
from .forms import  BookForm, DeleleBookForm

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)

def register(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("list_books_url")
    else:
        form= UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

            
def login_view(request):
    if request.method == "POST":
        form= AuthenticationForm(data= request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request, user)
            return redirect("list_books_url")
    else:
        form= AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

class LibraryDetailView(DetailView):
    queryset= Library.objects.get(name= "alx_library")
    template_name= "relationship_app/library_detail.html"
    context_object_name= "library"


def admin_check(user):
    return getattr(user, "userprofile", None) and user.userprofile.role == "Admin"

def librarian_check(user):
    return getattr(user, "userprofile", None) and user.userprofile.role == "Librarian"

def member_check(user):
    return getattr(user, "userprofile", None) and user.userprofile.role == "Member"



@user_passes_test(admin_check, "login")
def admin_view(request):
    render(request, "relationship_app/admin_view.html")

@user_passes_test(librarian_check, "login")
def librarian_view(request):
    render(request, "relationship_app/librarian_view.html")

@user_passes_test(member_check, "login")
def member_view(request):
    render(request, "relationship_app/member_view.html")

@permission_required("relationship_app.can_add_book", login_url="login")
def add_book_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("list_books_url")
    else:
        form = BookForm()
    
    return render(request, "relationship_app/add-book.html", {"form": form})

@permission_required("relationship_app.can_change_book", login_url="login")
def change_book_view(request):
    BookForm = modelform_factory(Book, fields=["title"])
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("list_books_url")
    else:
        form = BookForm()
    
    return render(request, "relationship_app/change-book.html", {"formset": form})

@permission_required("relationship_app.can_delete_book", login_url="login")
def delete_book_view(request):
    if request.method == "POST":
        form = DeleleBookForm(request.POST)
        book  = Book.objects.get(title= request.POST.get("title"))
        if book:
            book.delete()
            redirect("list_books_url")
    else:
        form= DeleleBookForm()
    
    return render(request, "relationship_app/delete-book.html", {"form": form})
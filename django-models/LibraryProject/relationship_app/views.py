from django.shortcuts import render, redirect
from django.forms import modelformset_factory, modelform_factory
from django.views.generic import ListView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test, permission_required
from .models import Book, Library, UserProfile
from .forms import  BookForm, DeleleBookForm

# Create your views here.

def get_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "list_books.html", context)

def register_view(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("list_books_url")
    else:
        form= UserCreationForm()
    return render(request, "register.html", {"form": form})

            
def login_view(request):
    if request.method == "POST":
        form= AuthenticationForm(data= request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request, user)
            return redirect("list_books_url")
    else:
        form= AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request, "logout.html")

class LibraryListView(ListView):
    queryset= Library.objects.get(name= "alx_library")
    template_name= "library_detail.html"
    context_object_name= "library"


def is_admin(user):
    return getattr(user, "userprofile", None) and user.userprofile.role == "Admin"

def is_librarian(user):
    return getattr(user, "userprofile", None) and user.userprofile.role == "Librarian"

def is_member(user):
    return getattr(user, "userprofile", None) and user.userprofile.role == "Member"



@user_passes_test(is_admin, "login")
def admin_view(request):
    render(request, "admin_view.html")

@user_passes_test(is_librarian, "login")
def librarian_view(request):
    render(request, "librarian_view.html")

@user_passes_test(is_member, "login")
def member_view(request):
    render(request, "member_view.html")

@permission_required("can_add_book", login_url="login")
def add_book_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("list_books_url")
    else:
        form = BookForm()
    
    return render(request, "add-book.html", {"form": form})

@permission_required("can_change_book", login_url="login")
def change_book_view(request):
    BookForm = modelform_factory(Book, fields=["title"])
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("list_books_url")
    else:
        form = BookForm()
    
    return render(request, "change-book.html", {"formset": form})

def delete_book_view(request):
    if request.method == "POST":
        form = DeleleBookForm(request.POST)
        book  = Book.objects.get(title= request.POST.get("title"))
        if book:
            book.delete()
            redirect("list_books_url")
    else:
        form= DeleleBookForm()
    
    return render(request, "delete-book.html", {"form": form})
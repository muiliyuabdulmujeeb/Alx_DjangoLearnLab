from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView, login_view, logout_view, admin_view, librarian_view, member_view, add_book_view, change_book_view, delete_book_view

urlpatterns = [
    path("books/", list_books, name="get_books_url"),
    path("library/", LibraryDetailView.as_view(), name= "list_books_url"),
    path("register/", views.register, name= "register"),
    path("login/", LoginView.as_view(template_name= "relationship_app/login.html", success_url= "books"), name= "login"),
    path("logout/", LogoutView.as_view(template_name= "relationship_app/logout.html"), name= "logout"),
    path("admin-view/", admin_view, name= "admin-view"),
    path("librarian-view/", librarian_view, name= "librarian-view"),
    path("member-view/", member_view, name= "member-view"),
    path("add_book/", add_book_view, name= "add-book-view"),
    path("edit_book/", change_book_view, name= "edit-book-view"),
    path("delete_book/", delete_book_view, name= "delete-book-view")
]
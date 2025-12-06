from django.urls import path
from .views import CreateView, DetailView, UpdateView, ListView, DeleteView


urlpatterns = [
    path("/books/", CreateView.as_view(), name="create_view"),
    path("/books/", ListView.as_view(), name="list_view"),
    path("/books/<int: pk>", DetailView.as_view(), name="detail_view"),
    path("/books/<int: pk>", UpdateView.as_view(), name="update_view"),
    path("/books/<int: pk>", DeleteView.as_view(), name="delete_view"),
]
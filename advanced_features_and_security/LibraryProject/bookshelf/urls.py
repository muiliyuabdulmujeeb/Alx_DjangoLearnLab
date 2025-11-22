from django.urls import path
from .views import create_article, view_article, edit_article, delete_article


urlpatterns = [
    path("create-article/", create_article, name= "create-article"),
    path("articles/", view_article, name= "articles"),
    path("edit-article/", edit_article, name= "edit-article"),
    path("delete-article/", delete_article, name= "delete-article")
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, create_user, user_profile, BlogPostCreateView, BlogPostUpdateView, BlogPostListView, BlogPostDetailView, BlogPostDeleteView, CommentCreateView, CommentDeleteView, CommentListView, CommentUpdateView


urlpatterns= [
    #auth
    path('', home, name="home"),
    path('auth/login/', LoginView.as_view(), name="login"),
    path('auth/logout/', LogoutView.as_view(), name= "logout"),
    path('auth/register/', create_user, name= "register"),
    path('auth/profile/', user_profile, name= "profile"),
    #posts
    path('post/new/', BlogPostCreateView.as_view(), name= "create_blogpost"),
    path('posts/', BlogPostListView.as_view(), name= "blogposts"),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name= "detail_blogpost"),
    path('post/<int:pk>/update/', BlogPostUpdateView.as_view(), name= "update_blogpost"),
    path('post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name= "delete_blogpost"),
    #comments
    path('post/<int:pk>/comment/new', CommentCreateView.as_view(), name= "create_blogpost_comment"),
    path('post/<int:pk>/comments', CommentListView.as_view(), name= "blogpost_comment"),
    path('post/<int:pk>/comment/<int:comment_id>', BlogPostDeleteView.as_view(), name= "detail_blogpost_comment"),
    path('post/<int:pk>/comment/<int:comment_id>/update/', CommentUpdateView.as_view(), name= "update_blogpost_comment"),
    path('post/<int:pk>/comment/<int:comment_id>/delete/', CommentDeleteView.as_view(), name= "delete_blogpost_coment"),
]
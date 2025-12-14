from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, create_user, user_profile, BlogPostCreateView, BlogPostUpdateView, BlogPostListView, BlogPostDetailView, BlogPostDeleteView, CommentCreateView, CommentDeleteView, CommentListView, CommentUpdateView, SearchView, TagView


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
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name= "create_blogpost_comment"),
    path('post/<int:post_id>/comments', CommentListView.as_view(), name= "blogpost_comment"),
    path('post/<int:post_id>/comment/<int:pk>', BlogPostDeleteView.as_view(), name= "detail_blogpost_comment"),
    path('post/<int:post_id>/comment/<int:pk>/update/', CommentUpdateView.as_view(), name= "update_blogpost_comment"),
    path('post/<int:post_id>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name= "delete_blogpost_coment"),
    #tags and search
    path("search/", SearchView.as_view(), name="search"),
    path("tags/<str:tag_name>/", TagView.as_view(), name="tag")
]
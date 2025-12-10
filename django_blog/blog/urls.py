from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import create_user, user_profile


urlpatterns= [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name= "logout"),
    path('register/', create_user, name= "register"),
    path('profile/', user_profile, name= "profile"),
]
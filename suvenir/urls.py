from django.urls import path, include
from suvenir.views import main
from authorization.views import LoginView, LogoutView, register_view




urlpatterns = [
    path("", main, name="main"),
    path("users/login/", LoginView.as_view(), name='login'),
    path("users/logout/", LogoutView.as_view(), name='logout'),
    path("users/register/", register_view, name='register')
]
from django.urls import path
from .views import authorization, LoginView, register_view, LogoutView, account



urlpatterns = [
    path("another_login/", authorization, name="another_authorization"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", register_view, name = 'register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("account", account, name='account')
]

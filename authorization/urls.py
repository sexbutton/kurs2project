from django.urls import path
from .views import authorization, LoginView



urlpatterns = [
    path("another_login/", authorization, name="another_authorization"),
    path("login/", LoginView.as_view(), name="login")
]

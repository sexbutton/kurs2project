from django.urls import path, include
from suvenir.views import main
from authorization.views import LoginView, LogoutView, register_view
from .views import basket, new, sale, popular, liked




urlpatterns = [
    path("", main, name="main"),
    path("users/login/", LoginView.as_view(), name='login'),
    path("users/logout/", LogoutView.as_view(), name='logout'),
    path("users/register/", register_view, name='register'),
    path("basket/", basket, name='basket'),
    path("new/", new, name='new'),
    path("sale/", sale, name='sale'),
    path("popular/", popular, name='popular'),
    path("liked/", liked, name='liked'),
]
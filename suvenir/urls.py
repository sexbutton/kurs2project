from django.urls import path, include
from authorization.views import LoginView, LogoutView, register_view
from .views import *




urlpatterns = [
    path("", MainMethod.as_view(), name="main"),
    path("users/login/", LoginView.as_view(), name='login'),
    path("users/logout/", LogoutView.as_view(), name='logout'),
    path("users/register/", register_view, name='register'),
    path("cart/", cart, name='cart'),
    path("new/", new, name='new'),
    path("sale/", sale, name='sale'),
    path("popular/", popular, name='popular'),
    path("liked/", liked, name='liked'),
    path("category/<str:slug>/souvenirs/<int:id>", souvenirs, name='souvenirs'),
    path("cart/add/<int:product_id>/", cart_add, name='cart_add'),
    path("cart/remove/<int:cart_id>/", cart_remove, name='cart_remove'),
    path("cart/all_remove/", cart_all_remove, name='cart_all_remove'),
    path("category/", include('category.urls')),
    path('createform/', createform, name = 'createform')
]

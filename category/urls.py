from django.urls import path, include
from category.views import *

urlpatterns = [
    path("", category, name='category'),
    path("cloth/", cloth, name='cloth'),
    path("dishes/", dishes, name='dishes'),
    path("joke/", joke, name='joke'),
    path("paintings/", paintings, name='paintings'),
    path("toys/", toys, name='toys'),
]


from django.urls import path, include
from suvenir.views import main



urlpatterns = [
    path("", main, name="main")
]
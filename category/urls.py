from django.urls import path, include
from category.views import *

urlpatterns = [
    path("", category, name='category'),
    path("sets/", sets, name='sets'),
    path("sushiandrolls/", sushiandrolls, name='sushiandrolls'),
    path("lunchandcombo/", lunchandcombo, name='lunchandcombo'),
    path("drinks/", drinks, name='drinks'),
]


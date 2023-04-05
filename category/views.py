from django.shortcuts import render
from suvenir.models import Product, Category


def toys(request):
    category = Category.objects.filter(name = "Игрушки")[0]
    toys = Product.objects.filter(category = category)
    return render(request, 'category/toys.html', {"product": toys})

def paintings(request):
    category = Category.objects.filter(name = "Картины")[0]
    paintings = Product.objects.filter(category = category)
    return render(request, 'category/paintings.html', {"product": paintings})

def joke(request):
    category = Category.objects.filter(name = "Розыгрыши")[0]
    joke = Product.objects.filter(category = category)
    return render(request, 'category/joke.html', {"product": joke})

def dishes(request):
    category = Category.objects.filter(name = "Посуда")[0]
    dishes = Product.objects.filter(category = category)
    return render(request, 'category/dishes.html', {"product": dishes})

def cloth(request):
    category = Category.objects.filter(name = "Одежда")[0]
    cloth = Product.objects.filter(category = category)
    return render(request, 'category/cloth.html', {"product": cloth})

def category(request):
    category = Category.objects.all()
    return render(request, 'category/category.html', {"category": category})
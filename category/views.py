from django.shortcuts import render
from suvenir.models import Product, Category
from django.db.models import Q

def sets(request):
    category = Category.objects.filter(name = "Сеты")[0]
    paintings = Product.objects.filter(category = category)
    if request.GET.get("price") == None:
        return render(request, 'category/sets.html', {'product': paintings})
    elif request.GET.get("price") != None:
        paintings = Product.objects.filter(Q(price__lte = request.GET.get("price")) & Q(category = category))
        return render(request, 'category/sets.html', {"product": paintings})
    

def sushiandrolls(request):
    category = Category.objects.filter(name = "Роллы и Суши")[0]
    joke = Product.objects.filter(category = category)
    if request.GET.get("price") == None:
        return render(request, 'category/sushiandrolls.html', {'product': joke})
    elif request.GET.get("price") != None:
        joke = Product.objects.filter(Q(price__lte = request.GET.get("price")) & Q(category = category))
        return render(request, 'category/sushiandrolls.html', {"product": joke})

def lunchandcombo(request):
    category = Category.objects.filter(name = "Ланчи и комбо")[0]
    dishes = Product.objects.filter(category = category)
    if request.GET.get("price") == None:
        return render(request, 'category/lunchandcombo.html', {'product': dishes})
    elif request.GET.get("price") != None:
        dishes = Product.objects.filter(Q(price__lte = request.GET.get("price")) & Q(category = category))
        return render(request, 'category/lunchandcombo.html', {"product": dishes})

def drinks(request):
    category = Category.objects.filter(name = "Напитки")[0]
    cloth = Product.objects.filter(category = category)
    if request.GET.get("price") == None:
        return render(request, 'category/drinks.html', {'product': cloth})
    elif request.GET.get("price") != None:
        cloth = Product.objects.filter(Q(price__lte = request.GET.get("price")) & Q(category = category))
        return render(request, 'category/drinks.html', {"product": cloth})


def category(request):
    category = Category.objects.all()
    return render(request, 'category/category.html', {"category": category})
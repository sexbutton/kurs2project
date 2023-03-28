from django.shortcuts import render
from .models import Product

def main(request):
    product = Product.objects.all()
    return render(request, 'suvenir/main.html', {"product": product})

def basket(request):
    return render(request, 'suvenir/basket.html')

def new(request):
    return render(request, 'suvenir/new.html')

def sale(request):
    return render(request, 'suvenir/sale.html')

def popular(request):
    return render(request, 'suvenir/popular.html')

def liked(request):
    return render(request, 'suvenir/liked.html')
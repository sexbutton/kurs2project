from django.shortcuts import render
from .models import Product

def main(request):
    product = Product.objects.all()
    return render(request, 'main/main.html', {"product": product})
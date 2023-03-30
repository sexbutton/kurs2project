from django.shortcuts import render, HttpResponseRedirect
from .models import Product, Cart

def main(request):
    product = Product.objects.all()
    return render(request, 'suvenir/main.html', {"product": product})

def cart(request):
    cart = Cart.objects.all()
    return render(request, 'suvenir/cart.html', {"cart": cart})

def new(request):
    return render(request, 'suvenir/new.html')

def sale(request):
    return render(request, 'suvenir/sale.html')

def popular(request):
    return render(request, 'suvenir/popular.html')

def liked(request):
    return render(request, 'suvenir/liked.html')

def souvenirs(request, id):
    souvenirs = Product.objects.get(pk=id)
    return render(request, 'suvenir/souvenirs.html', {'souvenirs':souvenirs})

def cart_add(request, product_id):
    product = Product.objects.get(id = product_id)
    carts = Cart.objects.filter(user = request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user = request.user, product = product, quantity = 1)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
        






from django.shortcuts import render, HttpResponseRedirect
from .models import Product, Cart

def main(request):
    product = Product.objects.all()
    return render(request, 'suvenir/main.html', {"product": product})

def cart(request):
    cart = Cart.objects.filter(user = request.user)

    if len(cart) > 0:
        lencart = True
    else:
        lencart = False

    countproduct = 0
    for i in cart:
        countproduct += i.quantity

    fullprice = 0
    for i in cart:
        fullprice += i.quantity * i.product.price


    return render(request, 'suvenir/cart.html', {"cart": cart, "lencart": lencart, "countproduct": countproduct, "fullprice": fullprice})

def new(request):
    product = Product.objects.filter(new = True)
    return render(request, 'suvenir/new.html', {'product': product})

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

def cart_remove(request, cart_id):
    cart = Cart.objects.get(id = cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def cart_all_remove(request):
    cart = Cart.objects.filter(user = request.user)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
        






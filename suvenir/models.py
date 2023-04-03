from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    description = models.CharField(max_length=1000, null= True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='suvenir/imgproduct')
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default= None)
    sale = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    pricesale = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    new = models.BooleanField(default=False)

    def __str__(self):
        return f"Сувенир: {self.name}. Категория: {self.category.name}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username}. Продукт:{self.product.name}'

    



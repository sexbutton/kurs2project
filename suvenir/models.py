from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    img = models.ImageField(upload_to='suvenir/imgproduct')
    date = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank= False)
    created_at = models.DateTimeField(auto_now_add=True)



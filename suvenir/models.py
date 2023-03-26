from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    img = models.ImageField(upload_to='images')
    date = models.DateTimeField()
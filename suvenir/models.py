from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='suvenir/imgproduct')
    date = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)


    



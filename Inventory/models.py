from typing import Any
from django.db import models
from datetime import datetime
from Category.models import Category
from Customer.models import Customer
from Product.models import Product
from Vendors.models import Vendors


# Create your models here.
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True) # Foreign Key link
    vendor = models.CharField(max_length=50, null = True)
    quantity = models.IntegerField(default=0)
    price = models.CharField(max_length=50, null = True)
    status = models.CharField(max_length=50)
    restocked = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null = True)
    expiry = models.DateField(null = True, default=datetime.now)
    def __str__(self):
        return self.product

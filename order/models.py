from django.db import models
from typing import Any
from datetime import datetime
from Product.models import Product
from Customer.models import Customer


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    shipping_address= models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    instructions = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=100)
    indate= models.DateField(null = True, default=datetime.now)
    outdate = models.DateField(null = True, default=datetime.now)
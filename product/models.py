from typing import Any
from django.db import models
from datetime import datetime
from Category.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, null=True)
    description = models.TextField(null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True) # Foreign Key link
    quantity = models.IntegerField(default=0)
    mrp = models.CharField(max_length=50, default=0)
    discount = models.CharField(max_length=50, default=0)
    price = models.CharField(max_length=50, default=0)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='products/')
    added = models.DateField(null = True, default=datetime.now)
    updated = models.DateField(null = True, default=datetime.now)
    def __str__(self):
        return self.name
    
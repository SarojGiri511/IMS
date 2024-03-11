from typing import Any
from django.db import models
from datetime import datetime
from Category.models import Category
from vendors.models import vendors





# Create your models here.
class Inventory(models.Model):
    product = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True) # Foreign Key link
    vendor = models.CharField(max_length=50, null = True)
    quantity = models.IntegerField(default=0)
    price = models.CharField(max_length=50, null = True)
    status = models.CharField(max_length=50)
    restocked = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null = True)
    expiry = models.DateField(null = True, default=datetime.now)

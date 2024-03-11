from django.db import models
from typing import Any
from datetime import datetime


# Create your models here.
class order(models.Model):
    customer = models.CharField(max_length=100)
    product = models.CharField(max_length=50, null=True)
    shipping_address= models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    instructions = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=100)
    indate= models.DateField(null = True, default=datetime.now)
    outdate = models.DateField(null = True, default=datetime.now)
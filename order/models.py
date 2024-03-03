from django.db import models
from typing import Any


# Create your models here.
class order(models.Model):
    customer = models.CharField(max_length=100)
    shipping_address= models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    instructions = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=100)
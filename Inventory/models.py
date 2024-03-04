from typing import Any
from django.db import models


# Create your models here.
class Inventory(models.Model):
    product = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    no_of_items = models.IntegerField(default=0)
    price = models.CharField(max_length=50, null = True)
    status = models.CharField(max_length=50)
    restocked = models.CharField(max_length=50)
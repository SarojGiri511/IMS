from typing import Any
from django.db import models


# Create your models here.
class purchase(models.Model):
    product = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    number_of_items = models.IntegerField()
    price_per_unit = models.IntegerField()
    total = models.IntegerField()
    image = models.ImageField()

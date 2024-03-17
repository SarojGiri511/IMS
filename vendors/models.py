from typing import Any
from django.db import models



# Create your models here.
class Vendors(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.PositiveBigIntegerField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    action = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
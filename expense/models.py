from typing import Any
from django.db import models
from datetime import datetime


# Create your models here.
class expense(models.Model):
    categories = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    amount = models.PositiveBigIntegerField(default=0)
    date = models.DateField(null = True, default=datetime.now)
   
   
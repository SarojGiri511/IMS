from typing import Any
from django.db import models
from datetime import datetime


# Create your models here.
class addexpense(models.Model):
    categories = models.CharField(max_length=50)
    describtion = models.CharField(max_length=50)
    amount = models.PositiveBigIntegerField(default=0)
    date = models.DateField(null = True, default=datetime.now)
   
   
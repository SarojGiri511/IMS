from typing import Any
from django.db import models
from datetime import datetime
from  Category.models import Category


# Create your models here.
class Expense(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=50)
    amount = models.PositiveBigIntegerField(default=0)
    date = models.DateField(null = True, default=datetime.now)
   
   
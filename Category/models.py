from typing import Any
from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, default=True, null=True)
    parent = models.IntegerField(null=True, blank=True)
    description = models.TextField(null = True, blank=True)
    added = models.DateField(null = True, default=datetime.now)
    def __str__(self):
        return self.name
    
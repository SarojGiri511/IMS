from typing import Any
from django.db import models
from datetime import datetime


# Create your models here.
class vendors(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.PositiveBigIntegerField(default=0)
    email = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    
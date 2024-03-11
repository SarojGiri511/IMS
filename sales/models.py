from django.db import models
from datetime import datetime


class sales(models.Model):
    customer = models.CharField(max_length=50, null=True)
    product = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    vat = models.IntegerField(default=0)
    gtotal = models.IntegerField(default=0)
    date = models.DateField(null=True, default=datetime.now)

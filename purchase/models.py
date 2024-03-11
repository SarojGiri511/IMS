from django.db import models
from datetime import datetime


# Create your models here.
class purchase(models.Model):
    product = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    invoice = models.CharField(max_length=50, blank=True, null=True)
    items = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(null=True, blank=True, upload_to='purchases/')
    date = models.DateField(null = True, default=datetime.now)

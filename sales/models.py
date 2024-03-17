from django.db import models
from datetime import datetime
from Product.models import Product
from Customer.models import Customer



class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    vat = models.IntegerField(default=0)
    gtotal = models.IntegerField(default=0)
    date = models.DateField(null=True, default=datetime.now)

from django.db import models
from datetime import datetime
from typing import Any
from customer.models import customer
from product.models import Product

# Create your models here.
class sales(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, blank=True, null=True)
    product= models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    grandTotal= models.IntegerField(default=0)
    date = models.DateField(null=True, default=datetime.now)
    def __str__(self):
        return f"Sales of {self.product} to {self.customer} on {self.date}"
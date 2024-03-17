from django.db import models
from datetime import datetime
from  Product.models import Product
from Vendors.models import Vendors


# Create your models here.
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    vendor =  models.ForeignKey(Vendors, on_delete=models.CASCADE, null=True, blank=True)
    invoice = models.CharField(max_length=50, blank=True, null=True)
    items = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(null=True, blank=True, upload_to='purchases/')
    date = models.DateField(null = True, default=datetime.now)
def __str__(self):
        return self.product
from django.db import models
from datetime import datetime
from typing import Any

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100,null=True)
    company_name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    phone_no = models.IntegerField(default=0)
    pan_number = models.IntegerField(default=0)
    created = models.DateField(null=True,default=datetime.now)
    updated = models.DateField(null=True,default=datetime.now)
    def __str__(self):
        return self.name



    


    
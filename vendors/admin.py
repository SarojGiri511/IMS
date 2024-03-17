from django.contrib import admin
from .models import Vendors

class VendorsAdmin(admin.ModelAdmin):
    list_display = ('name','address','contact','email','action')

# Register your models here.
admin.site.register(Vendors, VendorsAdmin)



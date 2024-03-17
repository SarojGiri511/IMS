from django.contrib import admin
from .models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('product','vendor','price','items','total','image')

# Register your models here.
admin.site.register(Purchase, PurchaseAdmin)

from django.contrib import admin
from .models import Inventory


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product','quantity','price')
    search_fields = ['name']


# Register your models here.
admin.site.register(Inventory, InventoryAdmin)
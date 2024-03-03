from django.contrib import admin
from .models import purchase
class purchaseAdmin(admin.ModelAdmin):
    list_display = ('product','vendor','price_per_unit','number_of_items','total','image')

# Register your models here.
admin.site.register(purchase, purchaseAdmin)

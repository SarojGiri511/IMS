from django.contrib import admin
from .models import sales

class salesAdmin(admin.ModelAdmin):
    list_display =  ('customer','product', 'quantity','rate','total','discount','grandTotal','date')
    search_fields = ['customer','product']

# Register your models here.
admin.site.register(sales, salesAdmin)


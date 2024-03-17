from django.contrib import admin
from .models import Sales  # Assuming your model is named 'Sales', not Ssales'

class SalesAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'rate', 'total', 'cost', 'discount', 'gtotal', 'date')
    search_fields = ['name']

# Register your model with the custom admin class
admin.site.register(Sales, SalesAdmin)



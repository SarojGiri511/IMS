from django.contrib import admin
from .models import Order

class orderAdmin(admin.ModelAdmin):
    list_display = ('customer','shipping_address','status','note')

# Register your models here.
admin.site.register(Order, orderAdmin)


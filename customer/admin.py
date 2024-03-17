from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone_no','email',)

# Register your models here.
admin.site.register(Customer, CustomerAdmin)


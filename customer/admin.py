from django.contrib import admin
from .models import customer

class customerAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone_no','email',)

# Register your models here.
admin.site.register(customer, customerAdmin)


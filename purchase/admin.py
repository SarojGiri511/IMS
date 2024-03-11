from django.contrib import admin
from .models import purchase


class purchaseAdmin(admin.ModelAdmin):
    list_display = ('product','vendor','price','items','total','image')

# Register your models here.
admin.site.register(purchase, purchaseAdmin)

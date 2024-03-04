from django.contrib import admin
from .models import addexpense


class addexpenseAdmin(admin.ModelAdmin):
    list_display = ('categories','description','amount')

# Register your models here.
admin.site.register(addexpense, addexpenseAdmin)

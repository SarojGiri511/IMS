from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','added')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
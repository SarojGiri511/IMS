from django.contrib import admin
from .models import expense


class expenseAdmin(admin.ModelAdmin):
    list_display = ('categories','description','amount')

# Register your models here.
admin.site.register(expense, expenseAdmin)

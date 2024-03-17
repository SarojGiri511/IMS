from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('categories','description','amount')

# Register your models here.
admin.site.register(Expense, ExpenseAdmin)

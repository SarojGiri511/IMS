from django import forms
from .models import expense


class expenseForm(forms.ModelForm):

    class Meta:
        model = expense
        fields = '__all__' #All Fields
from django import forms
from .models import addexpense


class expenseForm(forms.ModelForm):

    class Meta:
        model = addexpense
        fields = '__all__' #All Fields
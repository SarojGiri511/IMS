from django import forms
from Sales.models import Sales


class SalesForm(forms.ModelForm):

    class Meta:
        model = Sales
        fields = '__all__' #All Field
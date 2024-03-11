from django import forms
from .models import purchase

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = purchase
        fields = '__all__' #All Fields
from django import forms
from .models import customer

class CustomerForm(forms.ModelForm):

    class Meta:
        model = customer
        fields = '__all__' #All Fields
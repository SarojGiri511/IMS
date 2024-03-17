from django import forms
from .models import Vendors

class VendorsForm(forms.ModelForm):

    class Meta:
        model = Vendors

        fields = '__all__' #All Fields
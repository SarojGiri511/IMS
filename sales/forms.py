from django import forms
from sales.models import sales


class salesForm(forms.ModelForm):

    class Meta:
        model = sales
        fields = '__all__' #All Field
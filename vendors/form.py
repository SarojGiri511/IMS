from django import forms
from .models import vendors

class vendorsForm(forms.ModelForm):

    class Meta:
        model = vendors

        fields = '__all__' #All Fields
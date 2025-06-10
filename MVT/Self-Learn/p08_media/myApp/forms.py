from django import forms
from .models import myModel

class myForm(forms.ModelForm):
    class Meta:
        model = myModel
        fields = '__all__'
        labels = {
            'img': 'Image for outer folder (Project)',
            'pic': 'Image for inner folder (App)',
        }
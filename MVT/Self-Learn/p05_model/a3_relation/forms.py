from django import forms
from .models import relationModel

class Relation_Form(forms.ModelForm):
    class Meta:
        model = relationModel
        fields = '__all__'
        labels = {
            'example': 'Speciality (example model)',
            'table': 'Category (myTable model)',
        }
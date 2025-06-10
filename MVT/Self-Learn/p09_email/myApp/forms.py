from . import models
from django import forms

class Email_Form(forms.ModelForm):
    class Meta:
        model = models.Email_Model
        exclude = ['id',]
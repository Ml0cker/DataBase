from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationData
        fields = '__all__'
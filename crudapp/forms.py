from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from django.forms import ModelForm
from .models import Employee

## Using ModelForm for getting fields from model to our form

class EmployeeForm(forms.ModelForm):
    class Meta: # meta data is to provide data about data
        model= Employee
        fields = '__all__'
        # include = ['Pass the required fields from Model']
        # exclude= ['Pass the field which you want to exclude from Model']
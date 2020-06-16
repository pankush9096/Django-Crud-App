from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from django.forms import ModelForm
from .models import Register

# def check(value):

#     if value[0].lower() != 'a':
#         raise forms.ValidationError("Name should Start with A")
#
#
# class Loginform(forms.Form):

#     name= forms.CharField(max_length=30, label="Enter your name", validators = [check])  # using user defined validators

#     email = forms.EmailField(max_length=30, label= "Enter your email" )

#     verify_email= forms.EmailField(max_length=30, label= "Re-Enter your email" )

#     text = forms.CharField(widget= forms.Textarea) # widget for empty textbox

#     # Using pre defined django  validators for password to check minimum length( min_lenght, message we want to give)

#     password = forms.CharField(widget=forms.PasswordInput,
#                                validators=[validators.MinLengthValidator(6, message=" Must be 6 Character")])
#
#     def clean(self):
#         email = self.cleaned_data['email']
#         verify = self.cleaned_data['verify_email']
#         if email != verify:
#             raise forms.ValidationError('Email Doesnot Match')
#
#     # def clean_password_Validator(self):
#     #     password = self.cleaned_data['password']
#     #     if len(password)>5:
#     #         raise forms.ValidationError("PLease provide less than 5 character")
#     #
#     #
#     # password = forms.CharField(widget= forms.PasswordInput, validators = [clean_password_Validator])
#

## Using ModelForm for getting fields from model to our form

class Loginform(forms.ModelForm):
    class Meta: # meta data is to provide data about data
        model= Register
        fields = '__all__'
        # include = ['Pass the required fields from Model']
        # exclude= ['Pass the field which you want to exclude from Model']




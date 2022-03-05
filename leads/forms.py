from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import User,Lead,Agent




class CreateLeadForm(ModelForm):
   class Meta:
      model= Lead
      fields =['first_name','last_name','age','email','country','source']
      widget= {
         'first_name':forms.TextInput(),
         'last_name': forms.TextInput(),
         'age':forms.NumberInput(),
         'email':forms.EmailInput(),
         'country': forms.Select(),
         'source':forms.Select(),
         #'agent':forms.Select(),
      }


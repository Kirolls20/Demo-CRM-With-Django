from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

# Customize auth  Login form 
class UserLoginForm(AuthenticationForm):
   def __init__(self,*args,**kwargs):
      super(UserLoginForm,self).__init__(*args,**kwargs)
   
   username= UsernameField(widget=forms.TextInput())
   password=forms.CharField(widget=forms.PasswordInput())


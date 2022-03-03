from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from leads.models import User, Lead, Agent

# Customize auth  Login form


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email', 'age', 'phone_number', 'job_title',  'profile_pic']
        # labels={
        #     'first_name':"",
        #     'last_name':'',
        #     'username':'',
        #     'email':'',
        #     'age':'',
        #     'phone_number':'',
        #     'job_title':'',
        #     'profile_pic':'Choose image ',
        #     'password':'',



        # }


        widget = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'age': forms.Select(),
            'phone_number': forms.TextInput(),
            'job_title': forms.TextInput(),
            # 'password': forms.PasswordInput(),
            # 'password1': forms.PasswordInput(),
            'profile_pic': forms.FileInput(),
        }

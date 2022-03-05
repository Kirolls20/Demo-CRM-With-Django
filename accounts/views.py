from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from leads.models import User
from .forms import UpdateUserForm
from django.urls import reverse_lazy,reverse
from .forms import CreateUserForm, UserLoginForm

# def user_login(request):
#    if not request.user.is_authenticated:
#       if request.method == 'POST':
#          form = UserLoginForm(request.POST)
#          if form.is_valid():
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user= authenticate(username=username,password=password)

#             if user is not None:
#                login(request, user)
#                messages.success(request,'Logged in successfully!')
#                return reverse_lazy('land')
#       else:
#          form = UserLoginForm()
#       return render(request,'registration/login.html',{'form':form})

class CreateUserView(generic.CreateView):
   template_name = 'registration/signup.html'
   form_class = CreateUserForm

   def get_success_url(self):
      return reverse_lazy('login')


# Craete User Profile View
class UserProfileView(LoginRequiredMixin, generic.DetailView):
   template_name = 'registration/user_profile.html'
   model = User
   context_object_name = 'user'
   queryset = User.objects.all()

# Update User Profile View


class UpdatUserProfileView(LoginRequiredMixin, generic.UpdateView):
   template_name = 'registration/update_user_profile.html'
   model = User
   form_class = UpdateUserForm

   def get_success_url(self):
      return reverse_lazy('login')


# Change User Password View
class UserChangePasswordView(LoginRequiredMixin, PasswordChangeView):
   template_name = 'registration/change-password.html'
   form_class = PasswordChangeForm

   def get_success_url(self):
      return reverse_lazy('login')

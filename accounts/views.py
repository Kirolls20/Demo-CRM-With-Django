from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views import generic
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

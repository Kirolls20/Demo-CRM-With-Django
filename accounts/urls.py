from django.urls import path
from django.contrib.auth import views as v
from .forms import UserLoginForm
from . import views




urlpatterns=[
    path('login/', v.LoginView.as_view(
      template_name= 'registration/login.html',
      authentication_form=UserLoginForm),name='login'),
    # path('login/',views.user_login,name='login'),
    path('logout/',v.LogoutView.as_view(),name='logout'),
    path('signup/newuser/', views.CreateUserView.as_view(), name='signup')


]

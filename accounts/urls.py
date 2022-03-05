from django.urls import path
from django.contrib.auth import views as v
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm
from . import views




urlpatterns=[
    path('login/', v.LoginView.as_view(
      template_name= 'registration/login.html',
      authentication_form=UserLoginForm),name='login'),
    # path('login/',views.user_login,name='login'),
    path('logout/',v.LogoutView.as_view(),name='logout'),
    path('signup/newuser/', views.CreateUserView.as_view(), name='signup'),
    # process for reset the password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html') ,name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_complete'),
    path('user_profile/<int:pk>/',views.UserProfileView.as_view(), name='user-profile'),
    path('user_profile/<int:pk>/update/',views.UpdatUserProfileView.as_view(), name='update-profile'),
    path('user_profile/<int:pk>/password/',views.UserChangePasswordView.as_view(), name='change-password'),


]

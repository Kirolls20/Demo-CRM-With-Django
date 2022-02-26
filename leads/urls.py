from django.urls import path 
from . import views

urlpatterns=[
   path('all/',views.ListLeadsView.as_view(),name="lead-list"),
]
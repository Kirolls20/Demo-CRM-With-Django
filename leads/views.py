from django.shortcuts import render
from django.views import generic
from .models import Lead,Agent
from django.contrib.auth.mixins import LoginRequiredMixin


# Create Landing Page view and the path in root urls
class LandingpageView(generic.TemplateView):
   template_name = 'landing.html'


# Create Lead List View 
class ListLeadsView(LoginRequiredMixin, generic.ListView):
   template_name= "lead_list.html"
   model= Lead
   context_object_name= 'lead_list'

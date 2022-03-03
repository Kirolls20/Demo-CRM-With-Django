from django.shortcuts import render
from django.views import generic
from .models import Lead,Agent
from .forms import CreateLeadForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy


# Create Landing Page view and the path in root urls
class LandingpageView(generic.TemplateView):
   template_name = 'landing.html'   


class ListLeadsView(LoginRequiredMixin, generic.ListView):
   template_name= "lead_list.html"
   model= Lead
   context_object_name= 'lead_list'

# Create New Lead View
class CreateLeadView(LoginRequiredMixin, generic.CreateView):
   model= Lead
   form_class= CreateLeadForm
   template_name= 'create_lead.html'

   # def get_context_data(self, **kwargs):
   #    context = super(CreateLeadView,self).get_context_data(**kwargs)
   #    context['agent'] = Agent.objects.filter(user=self.request.user)
   #    print(context)
   #    return context
   # redirect to lead list after creating new lead
   def get_success_url(self):
      return reverse_lazy('lead-list')

# Lead DetailView Class


class LeadDetailView(LoginRequiredMixin,generic.DetailView):
   template_name= 'lead_detail.html'
   model= Lead
   queryset= Lead.objects.all()
   

# Update Lead View Class
class LeadUpdateView(LoginRequiredMixin,generic.UpdateView):
   template_name='lead_update.html'
   model= Lead
   form_class = CreateLeadForm
   queryset = Lead.objects.all()
   
   def get_success_url(self):
      return reverse_lazy('lead-list')

   

#Delete Lead view Class
class LeadDeleteView(LoginRequiredMixin,generic.DeleteView):
   template_name='lead_delete.html'
   model= Lead
   
   def get_success_url(self):
      return reverse_lazy('lead-list')


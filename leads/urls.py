from django.urls import path 
from . import views

urlpatterns=[
   
   path('all/',views.ListLeadsView.as_view(),name="lead-list"),
   path('create/newlead/',views.CreateLeadView.as_view(),name='create-lead'),
   path('lead/<int:pk>/detail/',views.LeadDetailView.as_view(),name='lead-detail'),
   path('lead/<int:pk>/update/',views.LeadUpdateView.as_view(),name='lead-update'),
   path('lead/<int:pk>/delete/',views.LeadDeleteView.as_view(),name='lead-delete'),
   path('user_lead/', views.ShowUserLeadView.as_view(),name='user-leads'),
   
  
   
   
]
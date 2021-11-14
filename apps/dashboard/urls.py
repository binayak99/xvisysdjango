from django import views
from django.urls import path, include
from django.conf.urls import url

from .api import api_search
from .views import  add_event, dashboard, event_detail, apply_for_event,search,edit_event,event_csv


urlpatterns = [
    
    path('api/search/', api_search, name='api_search'),
    path('search/', search, name='search'),
    path('', dashboard, name='dashboard'),
    path('add/', add_event, name='add_event'),
    #path('event_csv', event_csv, name='event_csv'),
    path('<int:event_id>/', event_detail, name='event_detail'),
    path('<int:event_id>/edit/', edit_event, name='edit_event'),
    path('<int:event_id>/apply_for_event/', apply_for_event, name='apply_for_event'),
]

 

 
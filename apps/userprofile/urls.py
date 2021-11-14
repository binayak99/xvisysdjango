
from django.urls import path, include
from . import views
from .views import admindashboard, view_dashboard_event, view_application,base, family_list, family_form, family_delete,area_list, area_form, area_delete, event_list, event_form, event_delete

urlpatterns = [
    path('', admindashboard, name='admindashboard'),
    path('event/<int:event_id>/', view_dashboard_event, name='view_dashboard_event'),
    path('application/<int:application_id>/', view_application, name='view_application'),
    path('base/',base, name='base'),
    path('insert/',views.family_form, name='family_insert' ),
    path('<int:id>',views.family_form, name='family_update'),
    path('delete/<int:id>',views.family_delete, name='family_delete'),
    path('list/',views.family_list, name='family_list'),
    path('ainsert/',views.area_form, name='area_insert' ),
    path('b<int:id>',views.area_form, name='area_update'),
    path('adelete/<int:id>',views.area_delete, name='area_delete'),
    path('alist/',views.area_list, name='area_list'),
    path('binsert/',views.event_form, name='event_insert' ),
    path('c<int:id>',views.event_form, name='event_update'),
    path('bdelete/<int:id>',views.event_delete, name='event_delete'),
    path('blist/',views.event_list, name='event_list'),
    path('front_page/',views.frontpage,name='front_page'),
]
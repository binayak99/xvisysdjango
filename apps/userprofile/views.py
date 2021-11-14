from apps.notification.utilities import create_notification
from apps.userprofile.models import ConversationMessage
from apps.dashboard.models import Application
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from apps.dashboard.models import Event, Application
from .models import ConversationMessage
from .forms import FamilyForm, AreaForm, EventForm
from .models import Family, VolunteerArea, VolunteerEvent

# Create your views here.
@login_required
def admindashboard(request):
    return render(request, 'userprofile/admindashboard.html', {'userprofile': request.user.userprofile})


@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_admin:
        application = get_object_or_404(Application, pk=application_id, event__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)
    
    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application=application, content=content, created_by=request.user)

            create_notification(request, application.created_by, 'message', extra_id=application.id)

            return redirect('view_application', application_id=application_id) 

    return render(request, 'userprofile/view_application.html',{'application': application})


@login_required
def view_dashboard_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id, created_by=request.user)

    return render(request, 'userprofile/view_dashboard_event.html', {'event': event})

@login_required
def base(request):
    return render(request, 'userprofile/base.html',{})

def family_list(request):
  context = {'family_list':Family.objects.all()}
  return render(request,"userprofile/family_list.html", context)

def family_form(request,id=0):
  if request.method == "GET":
    if id==0:
     form = FamilyForm()
    else:
     family = Family.objects.get(pk=id)
     form = FamilyForm(instance = family)
    return render(request,"userprofile/family_form.html",{'form':form})
  else: 
    if id == 0:
     form = FamilyForm(request.POST)
    else:
      family = Family.objects.get(pk=id)
      form = FamilyForm(request.POST,instance = family)
    if form.is_valid():
      form.save()
    return redirect('/family/list')

def family_delete(request, id):
  family = Family.objects.get(pk=id)
  family.delete()
  return redirect('/family/list')

def area_list(request):
  context = {'area_list':VolunteerArea.objects.all()}
  return render(request,"userprofile/area_list.html", context)

def area_form(request,id=0):
  if request.method == "GET":
    if id==0:
     form = AreaForm()
    else:
     volunteerarea = VolunteerArea.objects.get(pk=id)
     form = AreaForm(instance = volunteerarea)
    return render(request,"userprofile/area_form.html",{'form':form})
  else: 
    if id == 0:
     form = AreaForm(request.POST)
    else:
      volunteerarea = VolunteerArea.objects.get(pk=id)
      form = AreaForm(request.POST,instance = volunteerarea)
    if form.is_valid():
      form.save()
    return redirect('/family/alist')

def area_delete(request, id):
  volunteerarea = VolunteerArea.objects.get(pk=id)
  volunteerarea.delete()
  return redirect('/family/alist')

def event_list(request):
  context = {'event_list':VolunteerEvent.objects.all()}
  return render(request,"userprofile/event_list.html", context)

def event_form(request,id=0):
  if request.method == "GET":
    if id==0:
     form = EventForm()
    else:
     volunteerevent = VolunteerEvent.objects.get(pk=id)
     form = EventForm(instance = volunteerevent)
    return render(request,"userprofile/event_form.html",{'form':form})
  else: 
    if id == 0:
     form = EventForm(request.POST)
    else:
      volunteerevent = VolunteerEvent.objects.get(pk=id)
      form = EventForm(request.POST,instance = volunteerevent)
    if form.is_valid():
      form.save()
    return redirect('/family/blist')

def event_delete(request, id):
  volunteerevent = VolunteerEvent.objects.get(pk=id)
  volunteerevent.delete()
  return redirect('/family/blist')

def frontpage(request):
  return render(request,"userprofile/front_page.html")
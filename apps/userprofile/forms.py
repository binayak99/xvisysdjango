from django import forms
from .models import Family, VolunteerArea, VolunteerEvent

class FamilyForm(forms.ModelForm):

  class Meta:
    model = Family
    fields = '__all__'
    labels = {
      'parent1name' : 'Parent1 Name',
      'parent2name' : 'Parent2 Name',
      'homephone' : 'Home Phone No.',
      'businessphone' : 'Business Phone No.',
      'mailingaddress' : 'Mailing Address',
      'emailaddress' : 'Email Address',
    }

class AreaForm(forms.ModelForm):

  class Meta:
    model = VolunteerArea
    fields = '__all__'
    labels = {
      'volunteerareaid' : 'Area Id',
      'volunteerareaname' : 'Volunteer Area Name',
      'department' : 'Department',
    }
    

class EventForm(forms.ModelForm):

  class Meta:
    model = VolunteerEvent
    fields = '__all__'
    labels = {
      'eventdescription' : 'Volunteer Event',
      'eventdate' : 'eventdate',
      'eventstart' : 'eventstart',
      'eventend' : 'eventend',
      'volunteernumber ' : 'volunteernumber',
      'eventperiod' : 'Event Period',
    }
    

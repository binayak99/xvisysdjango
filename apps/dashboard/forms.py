from django import forms

from .models import Event, Application

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields =['title', 'short_description', 'long_description', 'start_time', 'end_time','volunteer_area']

    

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [ 'content', 'experience']

   
        
from django.contrib import admin

# Register your models here.
from .models import Event, Application

admin.site.register(Event)
admin.site.register(Application)


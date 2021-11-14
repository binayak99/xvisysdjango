from apps.dashboard.models import Application
from django.contrib.auth.models import User
from django.db import models

from apps.dashboard.models import Application

# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)


User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])

class ConversationMessage(models.Model):
    application = models.ForeignKey(Application, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

class Family(models.Model):
    parent1name = models.CharField(max_length=500)
    parent2name = models.CharField(max_length=500, blank=True)
    homephone = models.CharField(max_length=500)
    businessphone = models.CharField(max_length=500)
    mailingaddress = models.CharField(max_length=1000)
    emailaddress = models.CharField(max_length=500)

    

class VolunteerArea(models.Model):
    volunteerareaname = models.CharField(max_length=500)
    department = models.CharField(max_length=500)
    

    
 
class VolunteerEvent(models.Model):
    eventdescription = models.CharField(max_length=1000)
    eventdate = models.DateField()
    eventstart = models.TimeField()
    eventend = models.TimeField()
    volunteernumber = models.IntegerField()
    eventperiod = models.CharField(max_length=500)
    


from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Event(models.Model):

    ACTIVE = 'active'
    BOOKED = 'booked'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (BOOKED, 'Booked'),
        (ARCHIVED, 'Archived')
    )


    title = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    volunteer_area = models.CharField(max_length=255, null=True)

  

    created_by = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=ACTIVE)

    def __str__(self):
        return self.title

class Application(models.Model):
    event = models.ForeignKey(Event, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()

    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
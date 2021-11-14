from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, default='test')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('core:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
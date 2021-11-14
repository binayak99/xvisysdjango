import json 

from django.db.models import Q, query
from django.http import JsonResponse

from .models import Event

def api_search(request):
    eventslist = []
    data = json.loads(request.body)
    query = data['query']

    events = Event.objects.filter(status=Event.ACTIVE).filter(Q(title__icontains=query) | Q(short_description__icontains=query) | Q(long_description__icontains=query)) 

    for event in events:
        obj = {
            'id': event.id,
            'title': event.title,
            'short_description': event.short_description,
            'url': '/events/%s/' % event.id
        }
        eventslist.append(obj)

    return JsonResponse({'events': eventslist}) 

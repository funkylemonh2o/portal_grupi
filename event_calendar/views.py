from django.shortcuts import render
from .models import Event
# Create your views here.
import json
from django.core.serializers.json import DjangoJSONEncoder

def event_calendar_view(request):
    events = Event.objects.all().values('name', 'location', 'date', 'image_url')
    return render(request, 'event_calendar.html', {
        'events_json': json.dumps(list(events), cls=DjangoJSONEncoder)
    })
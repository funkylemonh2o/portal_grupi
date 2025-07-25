from django.shortcuts import render
from .models import Event
# Create your views here.
def event_calendar_view(request):
    events = Event.objects.all().order_by('date')  # or '-date' for newest first
    return render(request, 'event_calendar.html', {'events': events})
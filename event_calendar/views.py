from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_POST

def is_staff_user(user):
    return user.is_staff or user.is_superuser

def event_calendar_view(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events_calendar.html', {'events': events})

@login_required
@user_passes_test(is_staff_user)
@require_POST
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_calendar')

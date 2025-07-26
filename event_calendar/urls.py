from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.event_calendar_view, name='event_calendar')
]
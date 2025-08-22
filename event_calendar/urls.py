from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.event_calendar_view, name='event_calendar'),
    path('calendar/delete/<int:pk>/', views.event_delete, name='event_delete'),
]
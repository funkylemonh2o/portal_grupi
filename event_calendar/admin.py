from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date')
    search_fields = ('name', 'location')         # enable search
    ordering = ('-date',)                        # newest events first

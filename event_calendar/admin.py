from django.contrib import admin
from django.utils.html import format_html
from .models import Event
from .forms import EventForm


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = ('name', 'location', 'date', 'image_preview')
    search_fields = ('name', 'location')
    ordering = ('-date',)
    readonly_fields = ('image_preview',)

    fieldsets = (
        (None, {
            'fields': ('name', 'location', 'date')
        }),
        ('Image', {
            'fields': ('image', 'image_url', 'image_preview'),
            'description': 'You can either upload a local image file or provide an image URL.'
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius: 5px;" />', obj.image.url)
        return "No image"

    image_preview.short_description = 'Image Preview'


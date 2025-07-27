from django import forms
from .models import Event
from django.contrib.admin.widgets import AdminSplitDateTime


class EventForm(forms.ModelForm):
    image_url = forms.URLField(required=False, label="Image URL")

    class Meta:
        model = Event
        fields = ["name", "location", "date", "image"]
        widgets = {
            "date": AdminSplitDateTime(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].required = False
        self.fields["image"].help_text = "Upload a local image file"

    def save(self, commit=True):
        instance = super().save(commit=False)

        # If image_url is provided and no file is uploaded, handle URL
        image_url = self.cleaned_data.get("image_url")
        if image_url and not instance.image:
            # You can implement URL image download logic here if needed
            pass

        if commit:
            instance.save()
        return instance

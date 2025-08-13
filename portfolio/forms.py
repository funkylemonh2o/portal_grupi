from django import forms
from django.forms import inlineformset_factory
from .models import Portfolio, Media

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["title", "description", "github_link"]

MediaFormSet = inlineformset_factory(Portfolio, Media, fields=["file"], extra=1, can_delete=True)

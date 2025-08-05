from django import forms
from .models import Choice

class VoteForm(forms.Form):
    def init(self, question, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields["choice"] = forms.ModelChoiceField(
            queryset=question.choices.all(),
            widget=forms.RadioSelect,
            empty_label=None
        )
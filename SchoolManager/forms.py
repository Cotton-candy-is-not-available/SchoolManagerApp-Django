from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        widgets = {
            'date_of_event': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }
        fields = '__all__'


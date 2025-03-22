from django.contrib.auth.forms import UserCreationForm

from django.contrib .auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import Logs, Goal, Event
from operator import itemgetter

#------------------ Register/login ---------------------------

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)



# ------ Future Logs form -----
class CreateLogsForm(forms.ModelForm):
    class Meta:
        model = Logs
        fields = ['Log_name']

# -------- Goal form --------
class CreateGoalForm(forms.ModelForm):

    Importance = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=sorted(Goal.Order, key=itemgetter(0)),
    )
    class Meta:
        model = Goal
        fields = ['log','description', 'Importance']

#----------------- Events -------------------------
class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            # Makes the little box with dates appear
            widgets = {
            'date_of_event': forms.DateInput(format=('%m/%d/%Y'),
                                                 attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                        'type': 'date'}),
                'event_name': forms.TextInput(attrs={'class': 'form-control'}),

                'description': forms.TextInput(attrs = {'class': 'descriptionForm'}),
            }
            fields = '__all__'

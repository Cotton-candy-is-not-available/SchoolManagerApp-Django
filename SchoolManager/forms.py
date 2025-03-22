from django.contrib.auth.forms import UserCreationForm

from django.contrib .auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import Logs, Goal, Event

#------------------ Register/login ---------------------------

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)



# ------ To do list -----
class CreateLogsForm(forms.ModelForm):
    class Meta:
        model = Logs
        fields = ['Log_name']

# -------- Task form --------
class CreateGoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['log','description', 'Important', 'mid_important', 'least_important']

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

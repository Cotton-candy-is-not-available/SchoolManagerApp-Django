#copy and paste this code to Bita's

from django.contrib.auth.forms import UserCreationForm

from django.contrib .auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import Event

#------------------ Register/login ---------------------------
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)


#----------------- Events -------------------------
class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            # Makes the little box with dates appear
            widgets = {
            'date_of_event': forms.DateInput(format=('%m/%d/%Y'),
                                                 attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                        'type': 'date'}),
            }
            fields = '__all__'


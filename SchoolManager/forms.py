from django.contrib.auth.forms import UserCreationForm

from django.contrib .auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import TD_list, Task, Event, JournalEntry

from .models import Event


#------------------ Register/login ---------------------------

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)



# ------ To do list -----
class CreateListForm(forms.ModelForm):
    class Meta:
        model = TD_list
        fields = ['List_name']

# -------- Task form --------
class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['list','description', 'Important', 'mid_important', 'least_important']

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
            fields = ['event_name', 'description', 'date_of_event']

# -------- Journal Entry Form ------------
class EntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'writing'] #date will automatically be set to current date


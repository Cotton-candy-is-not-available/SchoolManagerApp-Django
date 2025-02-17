#copy and paste this code to Bita's

from django.contrib.auth.forms import UserCreationForm

from django.contrib .auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import TD_list, Task

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
        fields = '__all__'



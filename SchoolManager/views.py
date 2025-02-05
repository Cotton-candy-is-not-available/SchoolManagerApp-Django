from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event
from .forms import EventForm

def index(request):
    Events = Event.objects.all()

    event_form = EventForm()

    return render(request, 'index.html', {
        'event_form': event_form,


    })



def calendar(request):
    return render(request,'calendar.html')

def addEvent(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)

        #check if form is valid
        if event_form.is_valid():
            event_form.save()  #event to the database
            return redirect('calendar')
    else:
        event_form = EventForm() #GET request will simply render the form
    return render(request, 'event-form.html', {'event_form': event_form})
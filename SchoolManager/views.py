from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.html import escapejs

from .models import Event
from .forms import EventForm
from datetime import date, datetime, timedelta
from calendar import HTMLCalendar
import json

def index(request):
    event_form = EventForm()
    return render(request, 'index.html')


def displayEvents(request):
    events = Event.objects.all()
    return JsonResponse({"events": list(events.values())})



def calendar(request):
    events = Event.objects.all()
    return render(request, 'calendar.html', {'events': events})

def addEvent(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)

        if event_form.is_valid():
            #get the date_of_event from the POST data of the form
            date_of_event = request.POST.get('date_of_event')

            #set the date retrieved date_of_event to the form
            event_instance = event_form.save(commit=False)
            event_instance.date_of_event = date_of_event

            event_instance.save()
            return redirect('calendar')
        else:
            return HttpResponse("something went wrong with the event form")
    else:
        event_form = EventForm()  #for GET request, show the form
        return render(request, 'event-form.html', {'event_form': event_form})
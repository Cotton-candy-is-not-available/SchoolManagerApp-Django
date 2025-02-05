from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Calendar, Event
from .forms import EventForm
from datetime import date, datetime, timedelta
from calendar import HTMLCalendar


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

        if event_form.is_valid():
            calendar_id = request.POST.get('calendar_id')  #gets the calendar ID from the POST data

            #if a calendar ID is provided, associate the event with it
            if calendar_id:
                calendar = Calendar.objects.get(id=calendar_id)
                event = event_form.save()
                event.calendar = calendar  #associate the event with the calendar
                event.save()
            else:
                messages.error(request, "Calendar ID not provided.")
                return redirect('calendar')

            return redirect('calendar')
    else:
        event_form = EventForm()  #for GET request, show the form

    return render(request, 'event-form.html', {'event_form': event_form})
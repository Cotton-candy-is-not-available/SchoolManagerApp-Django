from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Calendar, Event
from .forms import EventForm

def index(request):
    Events = Event.objects.all()

    event_form = EventForm()

    return render(request, 'index.html', {
        'event_form': event_form,


    })

def calendar(request):
    from datetime import datetime
    current_month = datetime.now().month
    current_year = datetime.now().year
    days = Calendar.objects.filter(date__month=current_month, date__year=current_year)
    return render(request, 'calendar.html', {'days': days})

def addEvent(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)

        if event_form.is_valid():
            #retrieve the calendar day associated with the selected calendar day
            calendar_day = event_form.cleaned_data['day']

            event = event_form.save(commit=False)
            event.day = calendar_day  #link the event to the selected day
            event.save()

            return redirect('calendar')
    else:
        event_form = EventForm()

    return render(request, 'event-form.html', {'event_form': event_form})
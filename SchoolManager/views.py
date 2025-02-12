from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event
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

def switchMonths(request):

    #gets the current month
    current_date = datetime.now()
    month = int(request.GET.get('month', current_date.month))

    #all possible months
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    next_month = month + 1 if month < 12 else 1
    prev_month = month - 1 if month > 1 else 12

    return render(request, 'calendar.html',{
            'month': month,
            'month_name': months[month - 1],
            'next_month': next_month,
            'prev_month': prev_month,
    })

def addEvent(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)

        if event_form.is_valid():
            #get the date_of_event from the POST data of the form
            date_of_event = request.POST.get('date_of_event')

            #set the date retrieved date_of_event to the form
            event_instance = event_form.save(commit=False)
            event_instance.date_of_event = date_of_event  # Set the date

            event_instance.save()
            return redirect('calendar')
        else:
            return HttpResponse("something went wrong with the event form")

    else:
        event_form = EventForm()  #for GET request, show the form
        return render(request, 'event-form.html', {'event_form': event_form})
from time import strftime

from django.db.models.expressions import result
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate
from datetime import datetime, timedelta
from .models import Event
from .forms import EventForm

def start_page(request):
    return render(request, 'start_page.html')

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html')

def calendar(request):
    return render(request,'calendar.html')

#----- for register page -------#
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('index')

    return render(request, "register.html", {'form':form})

#-------- log in ------#

def log_in(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('index')

                #return HttpResponse('Logged in as %s' % user.username)

    context = {'form':form}

    return render(request, 'log_in.html', context=context)

#------- LOG OUT -----#

def user_logout(request):

    auth.logout(request)

    return redirect('start_page')

#------------------- Adding Events -------------------------
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
            return redirect('weekly_schedule')
        else:
            return HttpResponse("something went wrong with the event form")

    else:
        event_form = EventForm()  #for GET request, show the form
        return render(request, 'event-form.html', {'event_form': event_form})



# ----------------- weekly_schedule ------------------------

def weekly_schedule(request):

    weekDay = datetime.today()#gets today's date
    weekDay2 = datetime.today() + timedelta(days=1) #gets the day after
    weekDay3 = datetime.today() + timedelta(days=2)# gets the 3rd day after the first one

    #Filters to only get events that are associated with the same days
    day1_events = Event.objects.filter(date_of_event__day=weekDay.day, date_of_event__month =weekDay.month)
    day2_events = Event.objects.filter(date_of_event__day=weekDay2.day, date_of_event__month =weekDay2.month)
    day3_events = Event.objects.filter(date_of_event__day=weekDay3.day, date_of_event__month =weekDay3.month)

    context = {'weekDay':weekDay, 'weekDay2':weekDay2, 'weekDay3':weekDay3,
               'day1_events': day1_events, 'day2_events':day2_events, 'day3_events':day3_events}
    return render(request, 'weekly_schedule.html',context=context )


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate
from datetime import datetime, timedelta
from .models import Event
from .forms import EventForm

# global variables for next and prev buttons in weekly schedule
increase = 0
decrease = 0


def start_page(request):
    return render(request, 'start_page.html')


@login_required
def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})


@login_required
def calendar(request):
    return render(request, 'calendar.html')


# ----- for register page -------#
def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    return render(request, "register.html", {'form': form})


# -------- log in ------#

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

                # return HttpResponse('Logged in as %s' % user.username)

    context = {'form': form}

    return render(request, 'log_in.html', context=context)


# ------- LOG OUT -----#

def user_logout(request):
    auth.logout(request)

    return redirect('start_page')


# -------------------  Events -------------------------
# Add an event
@login_required
def addEvent(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        event_form.instance.user = request.user
        if event_form.is_valid():
            # get the date_of_event from the POST data of the form
            date_of_event = request.POST.get('date_of_event')

            # set the date retrieved date_of_event to the form
            event_instance = event_form.save(commit=False)
            event_instance.date_of_event = date_of_event

            event_instance.save()
            return redirect('weekly_schedule')
        else:
            return HttpResponse("something went wrong with the event form")
    else:
        event_form = EventForm()  # for GET request, show the form
        return render(request, 'weekly_schedule.html', {'event_form': event_form})

#View event
@login_required
def viewEvent(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'weekly_schedule.html',context=context)


# Update event
@login_required
def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('weekly_schedule')
    context = {'form': form}
    return render(request, 'weekly_schedule.html', context=context)


@login_required
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return redirect('weekly_schedule')


# ----------------- weekly_schedule ------------------------
# Figure out how to make duplicate code a function
# def events_of_the_day( request, day1, day2, day3):
#     # Filters to only get events that are associated with the same days
#     day1_events = Event.objects.filter(date_of_event__day=day1.day, date_of_event__month=day1.month)
#     day2_events = Event.objects.filter(date_of_event__day=day2.day, date_of_event__month=day2.month)
#     day3_events = Event.objects.filter(date_of_event__day=day3.day, date_of_event__month=day3.month)
#
#     context = {'day1_events':day1_events, 'day2_events':day2_events, 'day3_events':day3_events}
#     return render(request, 'weekly_schedule.html',context=context )

@login_required
def weekly_schedule(request):
    global decrease, increase
    increase = 0
    decrease = 0
    event_form = EventForm(request.POST)
    all_events = Event.objects.filter(user_id=request.user.id)
    weekDay = datetime.today()  # gets today's date
    weekDay2 = datetime.today() + timedelta(days=1)  # gets the day after
    weekDay3 = datetime.today() + timedelta(days=2)  # gets the 3rd day after the first one
    # Filters to only get events that are associated with the same days
    day1_events = Event.objects.filter(date_of_event__day=weekDay.day, date_of_event__month=weekDay.month,
                                       user_id=request.user.id)
    day2_events = Event.objects.filter(date_of_event__day=weekDay2.day, date_of_event__month=weekDay2.month,
                                       user_id=request.user.id)
    day3_events = Event.objects.filter(date_of_event__day=weekDay3.day, date_of_event__month=weekDay3.month,
                                       user_id=request.user.id)

    context = {'weekDay': weekDay, 'weekDay2': weekDay2, 'weekDay3': weekDay3,
               'day1_events': day1_events, 'day2_events': day2_events, 'day3_events': day3_events
        , 'event_form': event_form, 'all_events': all_events}
    return render(request, 'weekly_schedule.html', context=context)


# --------- Goes to dext few days ------------------
@login_required
def next_(request):
    global increase, decrease
    increase += 1
    event_form = EventForm(request.POST)
    weekDay = datetime.today() + timedelta(days=increase)  # gets today's date
    weekDay2 = datetime.today() + timedelta(days=1) + timedelta(days=increase)  # gets the day after
    weekDay3 = datetime.today() + timedelta(days=2) + timedelta(days=increase)  # gets the 3rd day after the first one
    decrease = increase
    # Filters to only get events that are associated with the same days
    day1_events = Event.objects.filter(date_of_event__day=weekDay.day, date_of_event__month=weekDay.month,
                                       user_id=request.user.id)
    day2_events = Event.objects.filter(date_of_event__day=weekDay2.day, date_of_event__month=weekDay2.month,
                                       user_id=request.user.id)
    day3_events = Event.objects.filter(date_of_event__day=weekDay3.day, date_of_event__month=weekDay3.month,
                                       user_id=request.user.id)

    context = {'weekDay': weekDay, 'weekDay2': weekDay2, 'weekDay3': weekDay3,
               'day1_events': day1_events, 'day2_events': day2_events, 'day3_events': day3_events,
               'event_form': event_form}
    return render(request, 'weekly_schedule.html', context=context)


# Goes to previous days
@login_required
def prev(request):
    global decrease, increase
    decrease -= 1
    event_form = EventForm(request.POST)
    weekDay = datetime.today() + timedelta(days=decrease)  # gets today's date
    weekDay2 = datetime.today() + timedelta(days=1) + timedelta(days=decrease)  # gets the day after
    weekDay3 = datetime.today() + timedelta(days=2) + timedelta(days=decrease)  # gets the 3rd day after the first one
    increase = decrease
    # Filters to only get events that are associated with the same days
    day1_events = Event.objects.filter(date_of_event__day=weekDay.day, date_of_event__month=weekDay.month,
                                       user_id=request.user.id)
    day2_events = Event.objects.filter(date_of_event__day=weekDay2.day, date_of_event__month=weekDay2.month,
                                       user_id=request.user.id)
    day3_events = Event.objects.filter(date_of_event__day=weekDay3.day, date_of_event__month=weekDay3.month,
                                       user_id=request.user.id)

    context = {'weekDay': weekDay, 'weekDay2': weekDay2, 'weekDay3': weekDay3,
               'day1_events': day1_events, 'day2_events': day2_events, 'day3_events': day3_events,
               'event_form': event_form}
    return render(request, 'weekly_schedule.html', context=context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import auth

from django.contrib.auth import authenticate
from datetime import datetime, timedelta
from .models import Event, Logs, Goal
from .forms import CreateUserForm, LoginForm, CreateGoalForm, CreateLogsForm, EventForm
from calendar import HTMLCalendar
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.html import escapejs
# global variables for next and prev buttons in weekly schedule
increase = 0
decrease = 0

def start_page(request):
    return render(request, 'start_page.html')


#Displays event in json format for the calendar
def displayEvents(request):
    events = Event.objects.filter(user_id=request.user.id)
    return JsonResponse({"events": list(events.values())})


@login_required
def calendar(request):
    events = Event.objects.filter(user_id=request.user.id)
    event_form = EventForm(request.POST)
    return render(request, 'calendar.html', {'events': events, 'event_form': event_form})

def addEvent(request ):
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
        return render(request, 'calendar.html', {'event_form': event_form})


# ----- for register page -------#
def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('calendar')

    return render(request, "register.html", {'form': form})

#     return render(request, "register.html", {'form': form})


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

                return redirect('calendar')

                # return HttpResponse('Logged in as %s' % user.username)

    context = {'form': form}

    return render(request, 'log_in.html', context=context)


# ------- LOG OUT -----#

def user_logout(request):
    auth.logout(request)

    return redirect('start_page')

# -------- Future logs and goals ------------#
# ----Goals-----
def create_goal(request):
    form = CreateGoalForm()
    if request.method == 'POST':
        form = CreateGoalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('FutureLogsGoals')

    context = {'form': form}
    return render(request, 'FutureLogs&Goals.html', context=context)

#delete Goals
def delete_goal(request, pk):
    goal = Goal.objects.get(id=pk)
    goal.delete()
    return redirect('FutureLogsGoals')


# ------- Logs --------
def create_logs(request):
    form_ = CreateLogsForm()
    if request.method == 'POST':
        form_ = CreateLogsForm(request.POST, request.FILES)
        if form_.is_valid():
            form_.save()
            return redirect('FutureLogsGoals')

    context = {'form_': form_}
    return render(request, 'FutureLogs&Goals.html', context=context)

def update_log_name(request, pk):
    log = Logs.objects.get(id=pk)
    form = CreateLogsForm(instance=log)
    if request.method == 'POST':
        form = CreateLogsForm(request.POST, instance=log)
        if form.is_valid():
            form.save()
            return redirect('FutureLogsGoals')
    context = {'form': form}
    return render(request, 'FutureLogs&Goals.html', context=context)


#Delete list
def delete_log(request, pk):
    log = Logs.objects.get(id=pk)
    log.delete()
    return redirect('FutureLogsGoals')


def FutureLogsGoals(request):
    log = Logs.objects.all()
    # log = Logs.objects.filter(user_id=request.user.id)
    # goals = Goal.objects.filter(user_id=request.user.id)
    goals = Goal.objects.all()
    logForm = CreateLogsForm()
    goalForm = CreateGoalForm()

    context = {'goals': goals, 'log': log, 'logForm': logForm, 'goalForm': goalForm}
    return render(request, 'FutureLogs&Goals.html', context=context)

def Toggle_task(request, goal_id):
    goals = Goal.objects.get(pk=goal_id)
    goals.completed = not goals.completed
    goals.save()
    return redirect('FutureLogsGoals')

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
    all_events = Event.objects.filter(user_id=request.user.id)
    event = Event.objects.get(id=pk)
    event_form = EventForm(instance=event)

    if request.method == 'POST':
        event_form = EventForm(request.POST, instance=event)
        if event_form.is_valid():
            event_form.save()
            return redirect('weekly_schedule')

    # Display events on edit page
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

    # context = {'event': event, 'all_events': all_events, 'event_form': event_form, 'test': test}
    return render(request, 'updateEvents.html', context=context)


def back_to_weekly(request):
    return redirect('weekly_schedule')


@login_required
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return redirect('weekly_schedule')


# ----------------- weekly_schedule ------------------------
#Displays events
def events_of_the_day( request, day1, day2, day3):
    # Filters to only get events that are associated with the same days
    day1_events = Event.objects.filter(date_of_event__day=day1.day, date_of_event__month=day1.month, user_id=request.user.id)
    day2_events = Event.objects.filter(date_of_event__day=day2.day, date_of_event__month=day2.month, user_id=request.user.id)
    day3_events = Event.objects.filter(date_of_event__day=day3.day, date_of_event__month=day3.month, user_id=request.user.id)

    context = {'day1_events':day1_events, 'day2_events':day2_events, 'day3_events':day3_events}
    return context

@login_required
def weekly_schedule(request):
    global increase, decrease
    increase = 0
    decrease = 0
    event_form = EventForm(request.POST)
    all_events = Event.objects.filter(user_id=request.user.id)
    weekDay = datetime.today()  # gets today's date
    weekDay2 = datetime.today() + timedelta(days=1)  # gets the day after
    weekDay3 = datetime.today() + timedelta(days=2)  # gets the 3rd day after the first one
    display_events = events_of_the_day(request, weekDay, weekDay2, weekDay3)
    context = {'weekDay': weekDay, 'weekDay2': weekDay2, 'weekDay3': weekDay3
        , 'event_form': event_form, 'all_events': all_events, 'display_events': display_events}
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
    display_events = events_of_the_day(request, weekDay, weekDay2, weekDay3)

    context = {'weekDay': weekDay, 'weekDay2': weekDay2, 'weekDay3': weekDay3
        , 'event_form': event_form, 'display_events': display_events}
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
    display_events = events_of_the_day(request, weekDay, weekDay2, weekDay3)

    context = {'weekDay': weekDay, 'weekDay2': weekDay2, 'weekDay3': weekDay3
        , 'event_form': event_form, 'display_events': display_events}
    return render(request, 'weekly_schedule.html', context=context)

@login_required
def stayOnCurrentPage(request):
    global increase, decrease
    event_form = EventForm(request.POST)
    weekDay = datetime.today() + timedelta(days=increase)  # gets today's date
    weekDay2 = datetime.today() + timedelta(days=1) + timedelta(days=increase)  # gets the day after
    weekDay3 = datetime.today() + timedelta(days=2) + timedelta(days=increase)  # gets the 3rd day after the first one
    # Filters to only get events that are associated with the same days
    display_events = events_of_the_day(weekDay, weekDay2, weekDay3)

    context = {'weekDay': weekDay, 'weekDay2': weekDay2, 'weekDay3': weekDay3
        , 'event_form': event_form, 'display_events': display_events}
    return render(request, 'weekly_schedule.html', context=context)

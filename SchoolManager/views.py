from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import auth

from django.contrib.auth import authenticate
from datetime import datetime, timedelta

from django.urls import reverse

from .models import Event, TD_list, Task
from .forms import CreateUserForm, LoginForm, CreateTaskForm, CreateListForm, EventForm
from calendar import HTMLCalendar, weekday
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
    events = Event.objects.all()
    return JsonResponse({"events": list(events.values())})


@login_required
def calendar(request):
    events = Event.objects.all()
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

            return redirect('index')

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

# -------- Todo_list ------------#
# ----Tasks-----
def create_task(request):
    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Todo_list')

    context = {'form': form}
    return render(request, 'Todo_list.html', context=context)

#delete Tasks
def delete_task(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return redirect('Todo_list')


# ------- List --------
def create_list(request):
    form_ = CreateListForm()
    if request.method == 'POST':
        form_ = CreateListForm(request.POST, request.FILES)
        if form_.is_valid():
            form_.save()
            return redirect('Todo_list')

    context = {'form_': form_}
    return render(request, 'Todo_list.html', context=context)

def update_list_name(request, pk):
    lists = TD_list.objects.get(id=pk)
    form = CreateListForm(instance=lists)
    if request.method == 'POST':
        form = CreateListForm(request.POST, instance=lists)
        if form.is_valid():
            form.save()
            return redirect('Todo_list')
    context = {'form': form}
    return render(request, 'Todo_list.html', context=context)


#Delete list
def delete_list(request, pk):
    lists = TD_list.objects.get(id=pk)
    lists.delete()
    return redirect('Todo_list')


def Todo_list(request):
    lists = TD_list.objects.all()
    task = Task.objects.all()
    listForm = CreateListForm()
    taskForm = CreateTaskForm()

    context = {'task': task, 'lists': lists, 'listForm': listForm, 'taskForm': taskForm}
    return render(request, 'Todo_list.html', context=context)

def Toggle_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('Todo_list')

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

@login_required
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return redirect('weekly_schedule')


# ----------------- weekly_schedule ------------------------
#Displays events
def events_of_the_day( day1, day2, day3):
    # Filters to only get events that are associated with the same days
    day1_events = Event.objects.filter(date_of_event__day=day1.day, date_of_event__month=day1.month)
    day2_events = Event.objects.filter(date_of_event__day=day2.day, date_of_event__month=day2.month)
    day3_events = Event.objects.filter(date_of_event__day=day3.day, date_of_event__month=day3.month)

    context = {'day1_events':day1_events, 'day2_events':day2_events, 'day3_events':day3_events}
    return context

@login_required
def weekly_schedule(request):
    event_form = EventForm(request.POST)
    all_events = Event.objects.filter(user_id=request.user.id)
    start_date = request.GET.get('date')

    print("Date1: ", start_date)

    if start_date:
        weekDay = datetime.strptime(start_date, "%Y-%m-%d")
    else:
        weekDay = datetime.today()  # gets today's date

    weekDay2 = weekDay + timedelta(days=1)  # gets the day after
    weekDay3 = weekDay + timedelta(days=2)  # gets the 3rd day after the first one
    print("Date2: ", start_date)
    print("weekday", weekDay)

    display_events = events_of_the_day(weekDay, weekDay2, weekDay3)
    context = {'weekDay': weekDay, 'weekDay2': weekDay2, 'weekDay3': weekDay3
        , 'event_form': event_form, 'all_events': all_events, 'display_events': display_events}
    return render(request, 'weekly_schedule.html', context=context)


# --------- Goes to next few days ------------------
@login_required
def next_(request):
    # weekDay = "2020-01-01" # gets today's date
    test = weekly_schedule(request)

    weekDay = datetime.today()+ timedelta(days=1)
    date_str = weekDay.strftime('%Y-%m-%d')

    print("test.weekday", test)

    # return redirect(reverse('weekly_schedule') + '?date'= weekDay)
    return redirect(reverse('weekly_schedule') + '?date={}'.format(date_str))


# Goes to previous days
@login_required
def prev(request):

    return redirect('weekly_schedule')


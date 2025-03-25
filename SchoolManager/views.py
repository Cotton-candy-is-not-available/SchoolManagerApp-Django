from typing import Protocol

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User

from datetime import datetime, timedelta, date
from .models import Event, TD_list, Task, Notification
from .forms import CreateUserForm, LoginForm, CreateTaskForm, CreateListForm, EventForm
from calendar import HTMLCalendar
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


from django.utils.html import escapejs
# global variables for next and prev buttons in weekly schedule

# For activation #

#from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage


increase = 0
decrease = 0

def start_page(request):
    return render(request, 'start_page.html')



@login_required
def index(request):
    event_form = EventForm()
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})



def displayEvents(request):
    events = Event.objects.all()
    return JsonResponse({"events": list(events.values())})


@login_required
def calendar(request):
    create_notifications(request.user)

    events = Event.objects.all()
    event_form = EventForm(request.POST)
    return render(request,
                  'calendar.html',
                  {'events': events, 'event_form': event_form,})


def addEvent(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        event_form.instance.user = request.user

        if event_form.is_valid():
            #get the date_of_event from the POST data of the form
            date_of_event = request.POST.get('date_of_event')
            #set the date retrieved date_of_event to the form
            event_instance = event_form.save(commit=False)
            event_instance.date_of_event = date_of_event

            event_instance.user = request.user

            event_instance.save()
            return redirect('calendar')
        else:
            return HttpResponse("something went wrong with the event form")
    else:
        event_form = EventForm()  #for GET request, show the form
        return render(request, 'calendar.html', {'event_form': event_form})

#----- ACTIVATE THE ACCOUNT ----#

#def activateEmail(request, user, to_email):
#    mail_subject = "Activate your user account"
#    message = render_to_string("template_activation.html", {
#        'user': user.username, #if doesn't work delete username
#        'domain': get_current_site(request).domain,
#        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#        'token': account_activation_token.make_token(user),
#        'protocol': 'https' if request.is_secure() else 'http',
#   })
#    email = EmailMessage(mail_subject, message, to=[to_email])
#    if email.send():
#        messages.success(request, f'Dear <b> {user} </b>, please'
#                              f'go to your email <b> {to_email} </b> inbox and click on \ '
#                              f'recieved activation link to confirm and complete the registration')
#   else:
#        messages.error(request, f'Problem sending email to {to_email}, check if'
#                                f'you typed it correctly.')

# def activate(request, uidb64, token):
#    User = get_user_model()
#    try:
#        uid = force_str(urlsafe_base64_decode(uidb64))
#        user = User.objects.get(pk=uid)
#    except:
#        user = None

#    if user is not None and account_activation_token.check_token(user, token):
#        user.is_active = True
#        user.save()
#        messages.success(request, f'Thank you! Your account has been activated')
#        return redirect ('login')
#    else:
#        messages.error(request, "Activation link is invalid!")

#    return redirect('start_page')


# ----- for register page -------#
def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

            #user = form.save(commit = False)
            #user.is_active = False
            #user.save()

            #activateEmail(request, user, form.cleaned_data.get ('email'))
            #return redirect('index')

        #else:
            #for error in list(form.errors.values()):
                #messages.error(request, error)


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


@login_required
def update_list_name(request, pk):
    lists = TD_list.objects.get(id=pk)
    form = CreateListForm(instance=lists)
    if request.method == 'POST':
        form = CreateListForm(request.POST, instance=lists)
        if form.is_valid():
            form.save()
            return redirect('Todo_list')  # can now update on index page and are shown to index
    context = {'form': form}
    return render(request, 'Todo_list.html', context=context)


#Delete list

@login_required
def delete_list(request, pk):
    lists = TD_list.objects.get(id=pk)
    lists.delete()
    return redirect('Todo_list')

@login_required
def Todo_list(request):
    lists = TD_list.objects.all()
    task = Task.objects.all()
    listForm = CreateListForm()
    taskForm = CreateTaskForm()

    context = {'task': task, 'lists': lists, 'listForm': listForm, 'taskForm': taskForm}
    return render(request, 'Todo_list.html', context=context)

@login_required
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
            event_instance.user = request.user
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
# @login_required
# def updateEvent(request, pk):
#     event = Event.objects.get(id=pk)
#     form = EventForm(instance=event)
#     if request.method == 'POST':
#         form = EventForm(request.POST, instance=event)
#         if form.is_valid():
#             form.save()
#             return redirect('weekly_schedule')
#     context = {'form': form}
#     return render(request, 'update_event_page.html', context=context)




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
    create_notifications(request.user)

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


#for sending email feature
#send_mail(
#    'Test Email from SchoolManager',
#    'This is a test email sent using Mailgun SMTP!',
#    None,  # Uses DEFAULT_FROM_EMAIL
#    ['your_verified_email@gmail.com'],  # Use a verified recipient for sandbox
#    fail_silently=False,
#)

#----NOTIFICATION FEATURE ----#
def create_notifications(user):
    today = date.today()
    upcoming_event = Event.objects.filter(
        user =user,
        date_of_event__gt=today,
        date_of_event__lte=today + timedelta(days=2)
    )
    print("Upcoming events found:", upcoming_event)

    for event in upcoming_event:

        message = f"Upcoming event: {event.event_name} on {event.date_of_event}"

        print("Checking event for notifications:", message)

        if not Notification.objects.filter(user=user, message=message).exists():
            print("Checking event for notifications:", message)
            Notification.objects.create(user=user, message=message)

            #filter(user=user, message__icontains=event.event_name, is_read=False).exists()):
            #message = f"Upcoming event: {event.event_name} on {event.date_of_event}"
            #Notification.objects.create(user=user, message=message)
            #message = f"Upcoming event: {event.event_name} on {event.date_of_event}").exists():
            #Notification.objects.create(user=user, message=message)


@login_required
def mark_notification_read(request, notif_id):
    notification = Notification.objects.get(id=notif_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect(request.META.get('HTTP_REFERER', 'calendar'))

@login_required
def mark_all_notifications_read(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return redirect(request.META.get('HTTP_REFERER', 'calendar'))

#Password for an email
#SCHOOL123
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate

def start_page(request):
    return render(request, 'start_page.html')

def index(request):
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
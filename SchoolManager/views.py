from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def calendar(request):
    return render(request,'calendar.html')

# for register page
def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form':form})

#log in

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

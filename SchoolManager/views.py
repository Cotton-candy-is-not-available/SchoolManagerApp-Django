from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, CreateTaskForm, CreateListForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate

from .models import TD_list, Task


def start_page(request):
    return render(request, 'start_page.html')


def index(request):
    return render(request, 'index.html')


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
            return redirect('Todo_list')  # can now update on index page and are shown to index
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


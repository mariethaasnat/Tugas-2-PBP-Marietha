import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from multiprocessing import context
from todolist.models import Task
from todolist.forms import NewToDoListForms

@login_required(login_url='/todolist/login/')
def show_todolist (request):
    if request.user.is_authenticated:
        data_todolist = Task.objects.filter(user = request.user)
        last_login = request.COOKIES.get('last_login', 'Not Found'),
        if (last_login == 'not found'):
            return redirect('todolist:login')
        context = {
            'todolist_item': data_todolist,
            'username': request.user.username,
            'last_login': request.COOKIES.get('last_login', 'Not Found'),
        }
        return render(request, "todolist.html", context)
    else:
        return render(request, 'todolist.html', context)

def register (request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user (request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def new_todolist (request):
    if request.user.is_authenticated:
        form = NewToDoListForms(request.POST)
        if request.method == 'POST' and form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task_baru = Task.objects.create(title=title, description=description,
                                                user=request.user, date=datetime.date.today())
            return redirect('todolist:show_todolist')
        
        context = {
            'form' : form,
        }
        return render(request, 'newtodolist.html', context)
    else:
        return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def new_todolist_ajax (request):
    if request.user.is_authenticated:
        form = NewToDoListForms(request.POST)
        response_data = {}
        if request.method == 'POST' and form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task_baru = Task.objects.create(title=title, description=description,
                                                user=request.user, date=datetime.date.today())
            response_data['title'] = title
            response_data['description'] = description
            response_data['date'] = datetime.date.today()
            return JsonResponse(response_data);

        context = {
            'form': form,
        }
        return render(request, 'newtodolist.html', context)
    else:
        return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def status_change (request, id):
    if request.user.is_authenticated:
        data_todolist = Task.objects.get(id=id)
        data_todolist.is_finished = not data_todolist.is_finished
        data_todolist.save()
        return redirect('todolist:show_todolist')
    else :
        return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def delete_task (request, id):
    if request.user.is_authenticated:
        Task.objects.filter(id=id).delete()
        return redirect('todolist:show_todolist')
    else :
        return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def get_data_json (request):
    data_todolist = Task.objects.filter(user = request.user)
    return HttpResponse (serializers.serialize("json", data_todolist), content_type = "application/json")
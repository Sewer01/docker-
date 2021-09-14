from main.forms import TaskForm
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    task = Task.objects.all()
    return render(request,'main/index.html', {'title': 'Главная', 'tasks': task})

def about(request):
    return render(request,'main/about.html')


def tabl(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: error = "ERROR"    

    form = TaskForm()
    context = {'form':form, 'error':error}
    return render(request,'main/tabl.html',context)
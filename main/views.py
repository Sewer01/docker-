from django.shortcuts import render
#from django.http import HttpResponse
from .models import Task

def index(request):
    task = Task.objects.all()
    return render(request,'main/index.html', {'title': 'Главная', 'tasks': task})

def about(request):
    return render(request,'main/about.html')


def tabl(request):
    return render(request,'main/tabl.html')
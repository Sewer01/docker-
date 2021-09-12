from django.shortcuts import render
from django.http import HttpResponse

def index(reguest):
    return HttpResponse("<h4> Hello Sergey!!! </h4>")

def about(reguest):
    return HttpResponse("<h4> My name Sergey!!! </h4>")

from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def hello_there(request):
    return HttpResponse("Hey, There.Hello")


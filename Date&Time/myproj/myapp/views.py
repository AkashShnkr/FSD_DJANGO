from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def DateAndTime(request):
    now=datetime.now();
    
    html ="<html><body>Current date {0}</body><html>".format(now)
    return HttpResponse(html)

# Create your views here.

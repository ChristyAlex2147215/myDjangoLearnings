from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def display(request):
    return HttpResponse("<h2>HELLO HIPPY</h2>")

def displaydatetime(request):
    dt=datetime.datetime.now()
    s="<b>Current date and time is:</b>"+str(dt)
    return HttpResponse(s)

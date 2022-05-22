from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rendertemplate(request):
    return render(request,'templatesapp/home.html',{"data":[1,2,3,4,5,6]})

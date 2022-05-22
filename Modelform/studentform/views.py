from django.shortcuts import render,redirect
from studentform import forms
from studentform import models
from studentform.forms import studentform
from studentform.models import student

# Create your views here.
def studentview(request):
    form=forms.studentform()
    if request.method=='POST':
        form=forms.studentform(request.POST)
        if form.is_valid():
            form.save()
            fname=form.cleaned_data['fname']
            lname=form.cleaned_data['lname']
            dob=form.cleaned_data['dob']
            password=form.cleaned_data['password']
            print(fname)
            print(lname)
            print(dob)
            print(password)
            return redirect('/successlogin')
    return render(request,'studentlogin.html',{'form':form})


def liststudents(request):
    s=student.objects.all()
    return render(request,'studenttable.html',{'s':s})

def successlogin_redirect(request):
    return render(request,'successlogin.html')

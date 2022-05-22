from django.shortcuts import render,redirect
from studentapp.models import Student
from studentapp.form import Studentform
# Create your views here.

def getstudents(request):
    student=Student.objects.all()
    return render(request,'student/index.html',{'student':student})

def createstudent(request):
    #form=Studentform()
    form=Studentform()
    if request.method=='POST':
        form=Studentform(request.POST)
        if form.is_valid():
            print(form.firstname)
            form.save()
        return redirect('/index')
    return render(request,'student/create.html',{'form':form})

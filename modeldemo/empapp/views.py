from django.shortcuts import render
from empapp.models import Employee
# Create your views here.
def employeedata(request):
    employee=Employee.objects.all()
    empDict={'employee':employee}
    return render(request,'employee.html',empDict)

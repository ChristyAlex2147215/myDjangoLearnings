from django import template
from empapp.model import Employee
register = template.Library()

@register.simple_tag
def my_tag():
    emp=Employee.objects.all();
    li=[]
    for i in emp:
        li.append(i.salary)
    return li    

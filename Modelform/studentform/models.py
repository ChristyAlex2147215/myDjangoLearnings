from django.db import models

# Create your models here.
class student(models.Model):
    fname=models.CharField(max_length=15)
    lname=models.CharField(max_length=15)
    dob=models.DateField()
    password=models.CharField(max_length=15)

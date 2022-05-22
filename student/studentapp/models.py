from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=30)
    secondname=models.CharField(max_length=30)
    testscore=models.FloatField()

from django.db import models



# Create your models here.
class Student(models.Model):
    email = models.EmailField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    course = models.CharField(max_length=100, null=False)
    message = models.TextField(max_length=200, null=True)


class AppliedStudent(models.Model):
    email = models.EmailField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    course = models.CharField(max_length=100, null=False)
    message = models.TextField(max_length=200, null=True)


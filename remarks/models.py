from django.db import models
from django import forms


# Create your models here.
class Remark(models.Model):
    email = models.EmailField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=True)
    message = models.TextField(max_length=250, null=False)

    remarks = models.CharField(max_length=100, null=True)

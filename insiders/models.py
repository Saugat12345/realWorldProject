from django.db import models

# Create your models here.
class Insider(models.Model):

    name = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    address = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    businessState = models.BooleanField(default=True)
    password = models.CharField(max_length=100, null=False)


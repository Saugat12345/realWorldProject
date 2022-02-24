from django.db import models

# Create your models here.
class MyAdmin(models.Model):

    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=100, null=False)
    is_superuser = models.BooleanField(default=False),
    last_login = models.DateTimeField(auto_now_add=True, null=True)

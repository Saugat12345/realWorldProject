from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.


class Order2(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    total_price = models.FloatField(default=0, null=True)
    quantity = models.IntegerField(default=1, null=True)
    remarks = models.TextField(max_length=250, null=True)
    product_name = models.CharField(null=False, max_length=200, default='noproduct')
    customer_name = models.CharField(null=False, max_length=200, default='noname')
class AutomobileOrder(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    total_price = models.FloatField(default=0, null=True)
    quantity = models.IntegerField(default=1, null=True)
    remarks = models.TextField(max_length=250, null=True)
    automobile_name = models.CharField(null=False, max_length=200, default='noautomobile')
    customer_name = models.CharField(null=False, max_length=200, default='noname')
class WorkerOrder(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    total_price = models.FloatField(default=0, null=True)
    remarks = models.TextField(max_length=250, null=True)
    worker_name = models.CharField(null=False, max_length=200, default='noworker')
    customer_name = models.CharField(null=False, max_length=200, default='noname')




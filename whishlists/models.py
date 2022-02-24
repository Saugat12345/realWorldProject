from django.db import models

# Create your models here.
class ProductWishlist(models.Model):
    date = models.DateTimeField(null=False)
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    customer_id = models.IntegerField()
    price = models.FloatField(default=1.1)
    product_id = models.IntegerField()
    product_status = models.CharField(max_length=100, default='unavailable')

class AutomobileWishlist(models.Model):
    date = models.DateTimeField(null=False)
    customer_name = models.CharField(max_length=100)
    automobile_name = models.CharField(max_length=100, default='truck')
    customer_id = models.IntegerField()
    price = models.FloatField(default=1.1)
    automobile_id = models.IntegerField()
    automobile_status = models.CharField(max_length=100, default='unavailable')

from django.db import models
STATUS_CHOICES = (
    ("available", "available"),
    ("unavailable", "unavailable"),
)
class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=100.55, null=True)
    image = models.FileField(null=True, upload_to='static/uploads')
    description = models.TextField(max_length=200, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available',
    )
class AppliedProduct(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=100.55, null=True)
    image = models.FileField(null=True, upload_to='static/uploads')
    description = models.TextField(max_length=200, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available',
    )
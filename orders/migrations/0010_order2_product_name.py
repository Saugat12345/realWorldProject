# Generated by Django 2.1.5 on 2021-09-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20210927_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='order2',
            name='product_name',
            field=models.CharField(default='noproduct', max_length=200),
        ),
    ]

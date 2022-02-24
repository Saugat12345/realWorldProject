# Generated by Django 2.1.5 on 2021-09-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]

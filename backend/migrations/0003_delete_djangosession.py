# Generated by Django 2.2.5 on 2020-06-02 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_authuser_djangosession'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DjangoSession',
        ),
    ]

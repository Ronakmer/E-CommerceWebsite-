# Generated by Django 4.0.4 on 2022-05-27 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='address',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='city',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='gmail',
        ),
    ]

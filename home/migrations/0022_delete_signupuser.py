# Generated by Django 4.0.4 on 2022-05-11 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_rename_user_signupuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='signupuser',
        ),
    ]

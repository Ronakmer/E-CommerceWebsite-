# Generated by Django 4.0.4 on 2022-05-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_customerservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerservice',
            name='cus_des',
            field=models.TextField(max_length=100),
        ),
    ]
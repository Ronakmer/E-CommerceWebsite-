# Generated by Django 4.0.4 on 2022-06-03 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_username_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='username',
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-03 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_user_order_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='username',
            new_name='user',
        ),
    ]

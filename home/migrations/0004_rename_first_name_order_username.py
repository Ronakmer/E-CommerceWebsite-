# Generated by Django 4.0.4 on 2022-06-03 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_order_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='username',
        ),
    ]

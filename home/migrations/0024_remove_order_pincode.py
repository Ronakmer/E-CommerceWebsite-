# Generated by Django 4.0.4 on 2022-06-07 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_order_total_alter_product_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pincode',
        ),
    ]

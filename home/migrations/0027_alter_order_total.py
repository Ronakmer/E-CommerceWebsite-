# Generated by Django 4.0.4 on 2022-06-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_alter_order_pincode_alter_order_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default='', max_length=50),
        ),
    ]

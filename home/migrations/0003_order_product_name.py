# Generated by Django 4.0.4 on 2022-06-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_order_product_image_order_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
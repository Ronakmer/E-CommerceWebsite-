# Generated by Django 4.0.4 on 2022-06-08 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_price',
            field=models.IntegerField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_qty',
            field=models.IntegerField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_qty',
            field=models.IntegerField(default='', max_length=200),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_product_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(default='', max_length=30),
        ),
    ]

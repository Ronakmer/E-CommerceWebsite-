# Generated by Django 4.0.4 on 2022-06-03 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_product_image_order_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='image',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='qty',
            new_name='product_qty',
        ),
    ]

# Generated by Django 4.2 on 2023-04-14 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Time',
        ),
    ]
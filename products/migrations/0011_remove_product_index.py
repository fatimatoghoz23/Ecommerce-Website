# Generated by Django 4.2 on 2023-04-15 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='index',
        ),
    ]
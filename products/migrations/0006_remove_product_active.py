# Generated by Django 4.2 on 2023-04-14 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_ram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
    ]

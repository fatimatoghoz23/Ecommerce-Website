# Generated by Django 4.2 on 2023-04-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_c'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='c',
        ),
        migrations.AddField(
            model_name='product',
            name='prrr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
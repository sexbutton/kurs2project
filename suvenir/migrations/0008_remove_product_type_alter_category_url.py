# Generated by Django 4.1.7 on 2023-05-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenir', '0007_type_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]

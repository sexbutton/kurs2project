# Generated by Django 4.1.7 on 2023-04-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenir', '0003_product_popular_product_sale_alter_product_pricesale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pricesale',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]

# Generated by Django 3.0.5 on 2024-06-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]

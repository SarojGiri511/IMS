# Generated by Django 5.0.2 on 2024-02-26 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0002_alter_product_thumbnail'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='product_id',
        ),
        migrations.AddField(
            model_name='sales',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AddField(
            model_name='sales',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
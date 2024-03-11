# Generated by Django 5.0.2 on 2024-03-10 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='number_of_items',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='price_per_unit',
        ),
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='invoice',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='items',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='total',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

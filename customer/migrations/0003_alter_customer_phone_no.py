# Generated by Django 5.0.2 on 2024-03-09 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.IntegerField(default=0),
        ),
    ]

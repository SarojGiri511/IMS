# Generated by Django 5.0.2 on 2024-03-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendors', '0002_alter_vendors_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='contact',
            field=models.PositiveBigIntegerField(max_length=15),
        ),
    ]

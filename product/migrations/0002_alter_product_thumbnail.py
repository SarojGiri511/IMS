# Generated by Django 5.0.2 on 2024-02-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
    ]
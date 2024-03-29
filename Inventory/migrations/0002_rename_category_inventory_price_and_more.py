# Generated by Django 5.0.2 on 2024-02-25 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='category',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='name',
            new_name='product',
        ),
        migrations.AddField(
            model_name='inventory',
            name='no_of_items',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='inventory',
            name='quantity',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='inventory',
            name='restocked',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='status',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]

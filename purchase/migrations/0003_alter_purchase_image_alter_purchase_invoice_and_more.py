# Generated by Django 5.0.2 on 2024-03-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_remove_purchase_number_of_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='purchases/'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='invoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='items',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

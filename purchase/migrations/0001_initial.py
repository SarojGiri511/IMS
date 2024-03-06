# Generated by Django 5.0.2 on 2024-03-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('vendor', models.CharField(max_length=50)),
                ('number_of_items', models.IntegerField()),
                ('price_per_unit', models.IntegerField()),
                ('total', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]

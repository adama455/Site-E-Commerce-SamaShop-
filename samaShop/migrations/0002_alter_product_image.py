# Generated by Django 4.2 on 2023-04-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samaShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=5000),
        ),
    ]

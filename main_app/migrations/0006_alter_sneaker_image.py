# Generated by Django 3.2.3 on 2021-06-07 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210607_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneaker',
            name='image',
            field=models.CharField(max_length=10000),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-01 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sneaker',
            name='created_at',
        ),
    ]

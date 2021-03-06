# Generated by Django 3.2.3 on 2021-06-03 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_remove_sneaker_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneaker',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sneaker',
            name='size',
            field=models.CharField(max_length=15),
        ),
    ]

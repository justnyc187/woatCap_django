from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Sneaker(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=550)
    size = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

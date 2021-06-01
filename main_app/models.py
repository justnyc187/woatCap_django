from django.db import models

# Create your models here.


class Sneaker(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=550)
    size = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

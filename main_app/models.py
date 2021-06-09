from django.db import models

from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Sneaker(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=10000)
    size = models.CharField(max_length=15)
    value = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # Do i need related name to connect sneakers to Profile as well as user?
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at', 'name']



# PROFILE MODEL FOR FUTURE

        # class Profile(models.Model):
#     name = models.CharField(max_length=500)
#     hometown = models.CharField(max_length=500)
#     favoriteShoe = models.CharField(max_length=200)
#     image = models.CharField(max_length=10000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['name']

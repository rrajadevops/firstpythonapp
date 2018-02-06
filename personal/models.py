from django.db import models

# Create your models here.

class hobby(models.Model):
    name = models.CharField(max_length=100)
    playercount = models.CharField(max_length=10)

class social(models.Model):
    activity = models.CharField(max_length=100)
    users = models.CharField(max_length=100)
from django.db import models


# Create your models here.

class hobby(models.Model):
    name = models.CharField(max_length=100)
    playercount = models.CharField(max_length=10)

    def __str__(self):
        return self.name + '-' + self.playercount


class social(models.Model):
    activity = models.CharField(max_length=100)
    users = models.CharField(max_length=100)

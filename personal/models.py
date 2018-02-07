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


class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album_logo = models.CharField(max_length=200)


class song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
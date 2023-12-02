from django.db import models

# Create your models here.
# playlists/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    # Додайте інші поля користувача за необхідності

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=[('private', 'Private'), ('public', 'Public')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Додайте інші поля плейлиста за необхідності

class Track(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    duration = models.IntegerField()
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    # Додайте інші поля трека за необхідності

from django.db import models

class Playlist(models.Model):
    # ваша модель Playlist
    class Meta:
        app_label = 'playlist'

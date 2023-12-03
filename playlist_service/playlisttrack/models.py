from django.db import models
from playlist.models import Playlist
from track.models import Track
from django.db import models

class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    # Додайте інші поля та зв'язки, які необхідні для вашого варіанту

    class Meta:
        app_label = 'playlisttrack'
        db_table = 'custom_playlisttrack_table'
        verbose_name = 'Custom PlaylistTrack'
        ordering = ['order']

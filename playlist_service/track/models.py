from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField()

    # Додайте інші поля та зв'язки для треків

    class Meta:
        app_label = 'playlist'
        db_table = 'custom_track_table'
        verbose_name = 'Custom Track'
        ordering = ['title']

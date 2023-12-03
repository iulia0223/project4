from django.db import models

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    # Додайте інші поля та зв'язки, які необхідні для вашого варіанту

    class Meta:
        app_label = 'playlist'  # Назва вашого додатку
        db_table = 'custom_playlist_table'  # Назва таблиці в базі даних
        verbose_name = 'Custom Playlist'  # Замість стандартної назви у адмінці
        ordering = ['title']  # Сортування за замовчуванням (в даному випадку, за полем title)

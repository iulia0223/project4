from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)

    # Додайте інші поля та зв'язки для користувача

    class Meta:
        app_label = 'user'
        db_table = 'custom_user_table'
        verbose_name = 'Custom User'
        ordering = ['username']

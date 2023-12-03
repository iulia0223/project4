from django.db import models

class User(models.Model):
    # ваша модель User
    class Meta:
        app_label = 'user'

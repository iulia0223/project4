# Generated by Django 4.2.7 on 2023-12-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlisttrack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlisttrack',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

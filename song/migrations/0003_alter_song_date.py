# Generated by Django 4.2.3 on 2023-07-22 05:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("song", "0002_song_album_alter_song_artist_alter_song_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 22, 0, 40, 10, 238180)
            ),
        ),
    ]
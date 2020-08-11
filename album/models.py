from django.db import models


class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'album'


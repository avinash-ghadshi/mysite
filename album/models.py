from django.db import models


class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'album'


class Tracks(models.Model):
    id = models.IntegerField(primary_key=True)
    album_id = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE, db_column='album_id')
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tracks'

from rest_framework import serializers
from .models import Album, Tracks

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class AlbumMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ( 'album_name', )


class TracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = '__all__'
        
class AlbumTracksSerializer(serializers.ModelSerializer):
    tracks = TracksSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')
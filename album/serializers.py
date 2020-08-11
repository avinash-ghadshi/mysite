from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class AlbumMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ( 'album_name', )

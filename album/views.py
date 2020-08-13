from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import AlbumSerializer, AlbumMiniSerializer, TracksSerializer, AlbumTracksSerializer
from album.models import Album, Tracks
from django.db.models import Q

# Create your views here.

#function based view
def test(request):
    return HttpResponse("HELLO WORLD!")

#class based view
class ListAlbum(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    
    allowed_methods = ( 'GET', 'POST', )
    
    def list(self, request):
        album_name = 'test'
        album_name1 = 'doori'
        queryset = Album.objects.all()
        #queryset = queryset.filter(Q(album_name=album_name) &
                                    #Q(album_name=album_name1))
        queryset = queryset.filter(album_name__endswith=album_name)
        
        #abname = ';select * from album'
        #queryset = Album.objects.raw("SELECT * FROM album where album_name=%s", [abname])
        print(queryset.query)
        serializer = AlbumSerializer(queryset,many=True)
        
        return Response(serializer.data)
            
class MiniListAlbum(viewsets.ModelViewSet):
    serializer_class = AlbumMiniSerializer
    queryset = Album.objects.all()
    
    allowed_methods = ( 'GET', )
    
class AlbumTracksViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumTracksSerializer;
    queryset = Album.objects.all();
    
    def get_queryset(self):
        queryset = Album.objects.all();
        #queryset = queryset.filter(tracks__title__contains='kadar')
        print("SQL>>>>>>>>"+ str(queryset.query))
        return queryset;
        
        
    
    # serializer_class = AlbumTracksSerializer;
    # queryset = Album.objects.all()
    
    # def get_queryset(self):
    #     queryset = Album.objects.all()
    #     print(queryset.query)
    #     return queryset
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serialized = AlbumTracksSerializer(queryset, many=True)
    #     return Response(serialized.data)
    
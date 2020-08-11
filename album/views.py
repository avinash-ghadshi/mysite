from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .serializers import AlbumSerializer, AlbumMiniSerializer
from album.models import Album

# Create your views here.

#function based view
def test(request):
    return HttpResponse("HELLO WORLD!")


#class based view
class ListAlbum(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    
    allowed_methods = ( 'GET', 'POST', )
    
class MiniListAlbum(viewsets.ModelViewSet):
    serializer_class = AlbumMiniSerializer
    queryset = Album.objects.all()
    
    allowed_methods = ( 'GET', )
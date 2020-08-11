from .views import test
from django.urls import path
from .views import ListAlbum, MiniListAlbum

urlpatterns = [
    path('test/', test),
    path('albumlist/', ListAlbum.as_view({'get': 'list', 'post': 'create'})),
    path('albumminilist/', MiniListAlbum.as_view({'get': 'list'})),
    #path('albumcreate/', ListAlbum.as_view({'post': 'create'})),
]

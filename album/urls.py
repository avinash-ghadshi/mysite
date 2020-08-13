from .views import test
from django.urls import path, include
from .views import ListAlbum, MiniListAlbum, AlbumTracksViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'albumlist', ListAlbum)
router.register(r'albumminilist', MiniListAlbum)
router.register(r'atlist', AlbumTracksViewSet)

urlpatterns = [
    path('test/', test),
    path('', include(router.urls))
    #path('albumlist/', ListAlbum.as_view({'get': 'list', 'post': 'create'})),
    #path('albumminilist/', MiniListAlbum.as_view({'get': 'list'})),
    #path('albumcreate/', ListAlbum.as_view({'post': 'create'})),
]

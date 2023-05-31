from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:aID>", views.ArtistsAlbums),
    path("<str:sort>", views.indexWithSort)
    # path("album<int:albumID>", views.album)
]
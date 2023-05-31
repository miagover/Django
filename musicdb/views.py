from django.shortcuts import render
from django.db import connection, connections
# from musicdb.models import Artist
# Create your views here.

def index(request):
    sqlQuery = "SELECT artist.id, artist.Name, artist.Formed, artist.website FROM artist ORDER BY name"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        connection.close()

    return render(request, "musicdb/index.html", {
        "artists": rows
    })

def ArtistsAlbums(request, aID):
    sqlQuery = "SELECT artist.id, album.id, artist.Name, album.AlbumName, album.YearReleased FROM artist INNER JOIN album ON artist.id = album.artistid AND artist.id = " + str(aID) + " ORDER BY album.YearReleased"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        connection.close()

    return render(request, "musicdb/artistalbums.html", {
        "albums": rows
    })

def indexWithSort(request, sort):
    sqlQuery = "SELECT artist.id, artist.Name, artist.Formed FROM artist ORDER BY " + sort
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        connection.close()

    return render(request, "musicdb/index.html", {
        "artists": rows
    })

def album(request, albumID):
    sqlQuery = "SELECT album.albumName, track.trackID, album.albumid, track.trackName, track.tracklength FROM album INNER JOIN track ON album.id = track.albumID AND album.id = " + str(albumID)
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        connection.close()

    return render(request, "musicdb/album.html", {
        "albumInfo": rows
    })
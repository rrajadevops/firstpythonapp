from django.http import HttpResponse
from .models import hobby, Album


def index(request):
    all_album = Album.objects.all()
    html = ''
    for album in all_album:
        url = '/personal/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)


def details(request, playercount):
    return HttpResponse("<h2>Details for playercount:" + str(playercount) + "</h2>")

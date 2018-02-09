#from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import hobby, Album
from django.core.exceptions import ObjectDoesNotExist


all_album = Album.objects.all()
context = {'all_album': all_album}
def index(request):
    #template = loader.get_template('personal/index.html')
    #return HttpResponse(template.render(context, request))
    return render(request, 'personal/index.html', {'all_album': all_album})


def details(request, playercount):
    album = get_object_or_404(Album, pk=playercount)
    return render(request, 'personal/details.html', {'album': album})
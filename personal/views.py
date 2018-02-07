from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import hobby, Album


def index(request):
    all_album = Album.objects.all()
    #template = loader.get_template('personal/index.html')
    context = {'all_album': all_album}
    #return HttpResponse(template.render(context, request))
    return render(request, 'personal/index.html', context)


def details(request, playercount):
    return HttpResponse("<h2>Details for playercount:" + str(playercount) + "</h2>")

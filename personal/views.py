from django.http import HttpResponse
def index(request):
    return HttpResponse("<h2>Name: <i>Rajasekaran Radhakrishnan</i></h2>")

def details(request, playercount):
    return HttpResponse("<h2>Details for playercount:" + str(playercount) + "</h2>")
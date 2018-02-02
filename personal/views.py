from django.http import HttpResponse
def index(request):
    return HttpResponse("<h2>Name: <i>Rajasekaran Radhakrishnan</i></h2>")
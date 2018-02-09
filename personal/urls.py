from django.urls import path, re_path
from . import views

app_name = 'personal'
urlpatterns = [
    #/personal/
    path('', views.index, name='index'),

    #/personal/777/
    re_path('^(?P<playercount>[0-9]+)/$', views.details, name='details'),
]

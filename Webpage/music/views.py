from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums':all_albums,
    }
    return  HttpResponse(template.render(context,request))

def detail(request,ablum_id):
    return HttpResponse("<h2>Details for Album id : " + str(ablum_id) + "</h2>")
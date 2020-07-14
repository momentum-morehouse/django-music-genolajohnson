from django.shortcuts import render
from .models import Album

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",       {"albums": albums})
  

def release_date(request):
    release = Release.objects.all()
    return render(request, "release/release_date.html",
                  {"release": release})
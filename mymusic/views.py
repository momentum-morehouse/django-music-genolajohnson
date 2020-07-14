from django.shortcuts import render
from .models import Album

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": albums})

# def add_album(request):
#     if request.method == 'GET':
#         form = ArtistAlbum()
#     else:
#         form = ArtistAlbum(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_artist')

#     return render(request, "artists/add_artist.html", {"form": form})   

def release_date(request):
    release = Release.objects.all()
    return render(request, "release/release_date.html",
                  {"release": release})
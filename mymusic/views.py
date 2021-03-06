from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Create your views here.
@login_required
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",       context={"albums": albums})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
    if form.is_valid():
        form.save()
        return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {
      "form": form,
      "album": album
      })

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_album.html",
                  {"album": album})   

def release_date(request):
    release = Release.objects.all()
    
    return render(request, "release/release_date.html",
                  {"release": release})

def add_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')
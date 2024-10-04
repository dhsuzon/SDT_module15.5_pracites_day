from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import AlbumModel

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        add_album = AlbumForm(request.POST)
        if add_album.is_valid():
            add_album.save()
            return redirect('add_album')
    else:
        add_album = AlbumForm()
    return render(request, 'album/add_album.html',{'form':add_album})





def edit_album(request,id):
    album = AlbumModel.objects.get(pk=id)
    if request.method == 'POST':
        add_album = AlbumForm(request.POST,instance=album)
        if add_album.is_valid():
            add_album.save()
            return redirect('add_album')
    else:
        add_album = AlbumForm(instance=album)
    return render(request, 'album/add_album.html',{'form':add_album})
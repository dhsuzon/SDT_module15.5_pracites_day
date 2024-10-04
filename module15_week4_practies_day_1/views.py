from django.shortcuts import render,redirect
from musician.models import MusicianModel
from album.models import AlbumModel
from album.forms import AlbumForm
from musician.models import MusicianModel
from musician.forms import MusicianForm

def show_data(request):
    # Get all musicians with their associated albums
    musicians = MusicianModel.objects.prefetch_related('albums').all()
    data = []

    for musician in musicians:
        for album in musician.albums.all():
            data.append({
                'musician_id': musician.id,
                'musician_name': f"{musician.First_Name} {musician.Last_name}",
                'email': musician.Email,
                'instrument_type': musician.Instrument_Type,
                'album_name': album.Album_Name,
                'album_rating': album.Rating_between,
                'album_release_date': album.Album_release_date,
                'album_id': album.id,
            })

    return render(request, "show_data.html", {'data': data})

def edit_album(request,id):
    album = AlbumModel.objects.get(pk=id)
    if request.method == 'POST':
        add_album = AlbumForm(request.POST,instance=album)
        if add_album.is_valid():
            add_album.save()
            return redirect('show_data')
    else:
        add_album = AlbumForm(instance=album)
    return render(request, 'album/add_album.html',{'form':add_album})


def edit_musician(request,id):
    m=MusicianModel.objects.get(pk=id)
    if request.method == 'POST':
        add_musician = MusicianForm(request.POST,instance=m)
        if add_musician.is_valid():
            add_musician.save()
            return redirect('show_data')
    else:
       add_musician = MusicianForm(instance=m) 
    return render(request, 'musician/add_musician.html',{'form':add_musician})

def delete_album(request,id):
    
    msician = MusicianModel.objects.get(pk=id)
    msician.delete()
    return redirect('show_data')
    
from django.shortcuts import render,redirect
from .forms import AlbumForm
from  .models import Albums
# Create your views here.
def add_album(request):
    if request.method=="POST":
        form= AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addAlbum')
    else:
        form= AlbumForm()
    return render(request, 'albums/albums.html', {'form': form})


# edit part

def edit_album(request, id):
    target= Albums.objects.get(pk= id)
    edit_form= AlbumForm(instance=target)
    if request.method=="POST":
        edit_form= AlbumForm(request.POST, instance=target)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('homePage')
    return render(request,  'albums/albums.html', {'form': edit_form} )

def delete_album(request, id):
    target= Albums.objects.get(pk= id).delete()
    return redirect('homePage')

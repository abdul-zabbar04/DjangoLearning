from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musicians

# Create your views here.
def add_musician(request):
    if request.method=="POST":
        form= MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addMusician')
    else:
        form= MusicianForm()
    return render(request, 'musicians/musicians.html', {'form': form})

def edit_musician(request, id):
    target= Musicians.objects.get(pk= id)
    edit_form= MusicianForm(instance=target)
    # print(edit_form)
    if request.method=="POST":
        edit_form= MusicianForm(request.POST, instance=target)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('homePage')
    return render(request, 'musicians/musicians.html', {'form': edit_form})

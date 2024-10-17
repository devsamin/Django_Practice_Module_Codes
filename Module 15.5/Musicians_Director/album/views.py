from django.shortcuts import render, redirect
from .models import AlbumModel
from album.forms import AlbumForm
# Create your views here.

# def album(request):
#     data = AlbumModel.objects.all()
#     print(data)
#     return render(request, 'albumfrom.html', {'data' : data})

def Album_Form(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('albumpage')

    else:
        form = AlbumForm()
    return render(request, 'albumfrom.html', {'form' : form})

def Edit_album(request, id):
    album = AlbumModel.objects.get(pk=id)
    edit_form = AlbumForm(instance=album)
    if request.method == 'POST':
        edit_form = AlbumForm(request.POST,instance=album)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('homepage')
    return render(request, 'albumfrom.html', {'form' : edit_form})

def delete_album(request, id):
    del_album = AlbumModel.objects.get(pk=id)
    del_album.delete()
    return redirect('homepage')
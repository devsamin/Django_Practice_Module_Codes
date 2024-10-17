from django.shortcuts import render, redirect
from musicians.models import MusicianModel
from musicians.forms import MusicianForm
# Create your views here.

# def musician(request):
#     data = MusicianModel.objects.all()
#     print(data)
#     return render(request, 'musicianfrom.html', {'data' : data})

def Musician_Form(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('musicianpage')

    else:
        form = MusicianForm()
    return render(request, 'musicianfrom.html', {'form' : form})

def Edit_musician(request, id):
    # print(id)
    album = MusicianModel.objects.get(Phone_Number=id)
    
    edit_form = MusicianForm(instance=album)
    if request.method == 'POST':
        edit_form = MusicianForm(request.POST,instance=album)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('homepage')
    return render(request, 'musicianfrom.html', {'form' : edit_form})


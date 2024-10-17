from django.shortcuts import render
from album.models import AlbumModel
from musicians.models import MusicianModel

# Create your views here.
def home(request):
    Adata = AlbumModel.objects.all()
    # Mdata = MusicianModel.objects.all()
    return render(request, 'home.html', {'Adata' : Adata})
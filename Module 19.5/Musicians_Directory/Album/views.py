from django.shortcuts import render
from django.views.generic import CreateView
from Album.models import AlbumModel
from Album.forms import AlbumForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required, name='dispatch')
class AlbumFormviews(CreateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = 'album/albumform.html'
    success_url = reverse_lazy('homepage')

@method_decorator(login_required, name='dispatch')
class EditViews(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = 'album/albumform.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

@method_decorator(login_required, name='dispatch')
class Deleteviews(DeleteView):
    model = AlbumModel
    template_name = 'album/delete_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
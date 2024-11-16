from django.shortcuts import render
from django.views.generic import CreateView
from musician.models import MusicianModel
from musician.forms import MusicianForm
from django.urls import reverse_lazy
# Create your views here.

class MusicianFormviews(CreateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'musician/musician_form.html'
    success_url = reverse_lazy('musician_list')
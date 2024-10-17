from django import forms
from musicians.models import MusicianModel

class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'
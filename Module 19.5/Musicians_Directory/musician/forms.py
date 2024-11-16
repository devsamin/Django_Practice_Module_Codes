from django import forms
from musician.models import MusicianModel

class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MusicianForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from Album.models import AlbumModel
from django import forms


class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
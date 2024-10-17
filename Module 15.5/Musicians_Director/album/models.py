from django.db import models
from musicians.models import MusicianModel
# Create your models here.
class AlbumModel(models.Model):
    Album_Name = models.CharField(max_length=20)
    Musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE )
    Release_Date = models.DateField()

    def __str__ (self):
        return self.Album_Name
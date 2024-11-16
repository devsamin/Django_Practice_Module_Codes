from django.db import models
from musician.models import MusicianModel
# Create your models here.

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField()
    RATING_CHOICES  = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    def __str__(self):
        return f"{self.album_name} by {self.musician}"
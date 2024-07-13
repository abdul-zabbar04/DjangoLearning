from django.db import models
from musician.models import MusicianModel

# Create your models here.
class AlbumModel(models.Model):
    album_name= models.CharField(max_length=50)
    musician= models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    album_release_date= models.DateField()
    choices= ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    rating= models.IntegerField(choices=choices)

    def __str__(self):
        return f'{self.album_name}-{self.musician.first_name}'
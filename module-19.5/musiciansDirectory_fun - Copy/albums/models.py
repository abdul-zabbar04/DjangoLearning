from django.db import models
from musicians.models import Musicians
import datetime
# Create your models here.
class Albums(models.Model):
    album_name= models.CharField(max_length=50)
    musician= models.ForeignKey(Musicians, on_delete=models.CASCADE)
    album_release_date= models.DateField()
    choices= ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    rating= models.IntegerField(choices=choices)

    def __str__(self):
        return f'{self.album_name}-{self.musician.first_name}'
from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField()
    phone= models.CharField(max_length=20)
    instruments= (('saxophone', 'Saxophone'), ('cello', 'Cello'),('clarinet','Clarinet'),
    ('harp','Harp'),('bass', 'Bass'),('guitar','Guitar'),('trombone','Trombone'))
    instrument_type= models.CharField(max_length=50, choices=instruments)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
from django.db import models

# Create your models here.
class demoModel(models.Model):
    big_int= models.BigIntegerField()
    bool_field= models.BooleanField()
    name= models.CharField(max_length=30)
    DOB= models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=6, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file= models.FileField(upload_to='file')
    slug_field = models.SlugField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()



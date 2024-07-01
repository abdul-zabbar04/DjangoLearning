from django.db import models
from author.models import AuthorModel
# Create your models here.
class ProfileModel(models.Model):
    author= models.OneToOneField(AuthorModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author.name

from django.db import models
from author.models import AuthorModel
from categories.models import CategoryModel
# Create your models here.
class PostModel(models.Model):
    title= models.CharField(max_length=20)
    content= models.TextField()
    
    author= models.ForeignKey(AuthorModel, on_delete= models.CASCADE)
    category= models.ManyToManyField(CategoryModel)

    def __str__(self):
        return f'{self.title}-{self.author}'
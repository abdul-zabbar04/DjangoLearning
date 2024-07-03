from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    categoryName= models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.categoryName
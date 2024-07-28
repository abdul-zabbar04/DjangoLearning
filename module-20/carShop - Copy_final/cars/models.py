from django.db import models
from brands.models import BrandModel
# Create your models here.
class CarModel(models.Model):
    image= models.ImageField(upload_to='cars/upload', blank=True, null=True, default='cars/upload/home.webp')
    title= models.CharField(max_length=100)
    description= models.TextField()
    price= models.CharField(max_length=20)
    quantity= models.PositiveIntegerField(null=True, blank=True, default=1)
    brand_name= models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class CommentModel(models.Model):
    car= models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name= models.CharField(max_length=50)
    body= models.TextField()
    create_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'comment by {self.name}'
    

    

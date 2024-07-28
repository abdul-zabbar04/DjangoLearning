from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BroughtCars(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    sold_car= models.IntegerField(null=True, blank=True)
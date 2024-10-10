from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Category: {self.name}'
    
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    isAvailable = models.BooleanField(defaul=True)

    def __str__(self):
        return f"Room: {self.name}"
    
class Booking(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
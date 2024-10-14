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
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return f"Room: {self.name}"
    
class Booking(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'Бронирование {self.room_id.name} пользователи {self.userID.username}'

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    rooms = models.ManyToManyField(Room, related_name='amenities')

    def __str__(self) ->str:
        return f"Amenity: {self.name}"
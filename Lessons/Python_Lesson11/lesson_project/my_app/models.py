from django.db import models
from re import T
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

class UserProfile(models.Model):
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __set__(self):
        return self.name

class BBoard(models.Model):
    title = models.CharField(max_length=50, verbose_name="название рекламы")
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"
        ordering = ['-published']

    def __str__(self):
        return self.title
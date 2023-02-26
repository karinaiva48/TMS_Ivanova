from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.TextField()
    second_name = models.TextField()
    login = models.TextField()
    email = models.EmailField()

class Category(models.Model):
    name = models.TextField()

class Post(models.Model):
    tittle = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

   
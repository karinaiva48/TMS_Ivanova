from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.TextField()
    second_name = models.TextField()
    login = models.TextField()
    email = models.EmailField()

    def __str__(self) -> str:
        return f'First name: {self.first_name}, Second name: {self.second_name}'


class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    tittle = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Post: {self.tittle}, category: {self.category}'
        
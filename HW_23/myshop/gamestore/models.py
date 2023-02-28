from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Category title')
    slug = models.SlugField(max_length=40, verbose_name='Category slug')
    description = models.CharField(max_length=150, verbose_name='Category description')
    is_active = models.BooleanField(verbose_name='Category is active')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Game(models.Model):
    name = models.CharField(max_length=100, verbose_name='Game name')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='Category game')
    description = models.CharField(max_length=150, verbose_name='Game description')
    is_active = models.BooleanField(default=True, verbose_name='Game is active')
    pub_date = models.DateTimeField(auto_now_add=True)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    slug = models.SlugField(max_length=40, verbose_name='Game slug')
    game_image = models.ImageField(upload_to='images/')
    

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('game', kwargs={'game_slug': self.slug})

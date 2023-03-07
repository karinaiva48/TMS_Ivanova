from django.db import models
from django.urls import reverse

class ShopInfoMixin(models.Model):
    slug = models.SlugField(max_length=40, verbose_name='Slug')
    is_active = models.BooleanField(verbose_name='Active', default=True)
    description = models.CharField(max_length=150, verbose_name='Description')

    class Meta:
        abstract = True

class Category(ShopInfoMixin):
    title = models.CharField(max_length=40, verbose_name='Category title')
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Game(ShopInfoMixin):
    name = models.CharField(max_length=100, verbose_name='Game name')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='Category game')
    pub_date = models.DateTimeField(auto_now_add=True)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    game_image = models.ImageField(upload_to='images/', null = True)
    

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        indexes = [models.Index(fields=['name'], name='name_index'),
                   models.Index(fields=['price'], name='price_index'),
                   models.Index(fields=['category'], name='category_index')
                   ]


    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('game', kwargs={'game_slug': self.slug})

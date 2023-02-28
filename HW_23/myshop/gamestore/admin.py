from django.contrib import admin
from gamestore.models import Category, Game

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    ...

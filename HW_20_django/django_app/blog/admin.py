from django.contrib import admin

from blog.models import User, Post, Category
# Register your models here.

@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'created_date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
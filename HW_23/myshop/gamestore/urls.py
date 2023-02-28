from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<slug:game_slug>', views.show_game, name='game'),
    path('category/<slug:category_slug>', views.show_category, name='category'),
]
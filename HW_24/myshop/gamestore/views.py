from django.shortcuts import render
from .models import *
from django.http import HttpRequest

def index(request: HttpRequest):
    sor = request.GET.get('sort', 'name')
    title = 'Home page'
    games = Game.objects.order_by(sor)
    category = Category.objects.order_by('title')
    return render(request, 'gamestore/index.html', {'title': title, 'games': games, 'category': category})


def show_category(request: HttpRequest, category_slug):
    sor = request.GET.get('sort', 'name')
    print(sor)
    title = 'Category'
    cat = Category.objects.order_by('title')
    games = Game.objects.filter(category__slug=category_slug).order_by(sor)
    return render(request, 'gamestore/index.html', {'title': title, 'games': games, 'category': cat})


def show_game(request, game_slug):
    title = 'Game'
    category = Category.objects.all()
    games = Game.objects.filter(slug=game_slug)
    return render(request, 'gamestore/show_game.html', {'title': title, 'games': games, 'category': category})
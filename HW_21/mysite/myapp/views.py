from django.shortcuts import render
from django.views.generic import View, TemplateView
import requests
from django.http import HttpRequest, HttpResponse
import json

class KanyeWestQuote(View):

    def get(self, request, *args, **kwargs):
        number = kwargs['number'] if kwargs.get('number') else 1
        quotes_list = [requests.get('https://api.kanye.rest').json()['quote'] for _ in range(int(number))]
        return render(request, 'myapp/quotes.html', {'quotes': quotes_list})

def index(request: HttpRequest):
    json.loads(request.body)
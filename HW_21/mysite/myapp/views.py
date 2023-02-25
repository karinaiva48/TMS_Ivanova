from django.shortcuts import render
from django.views.generic import View, TemplateView
import requests
from django.http import HttpRequest, HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404



class KanyeWestQuote(View):

    def get(self, request, *args, **kwargs):
        number = kwargs['number'] if kwargs.get('number') else 1
        quotes_list = [
            requests.get('https://api.kanye.rest').json()['quote'] for _ in range(int(number))
            ]
        return render(request, 'myapp/quotes.html', {'quotes': quotes_list})

    
def factorial_func(num):
    if num == 0:
        return 1
    else:
        return(num*factorial_func(num-1))

@csrf_exempt
@require_http_methods(['GET', 'POST'])
def index(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse('Введите число:')
    elif request.method == 'POST':
        number = json.loads(request.body)
        try:
            factorial = factorial_func(number.get('number'))
        except TypeError:
            raise Http404('Incorrect type of message')
        else:
            return render(request, 'myapp/index.html', {'number': number.get('number'), 'factorial': factorial})

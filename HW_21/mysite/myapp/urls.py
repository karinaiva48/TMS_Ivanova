from django.urls import path
from . import views

urlpatterns = [
    path('quotes/', views.KanyeWestQuote.as_view(), name='quotes'),
    path('quotes/number/<int:number>', views.KanyeWestQuote.as_view(), name='quotes'),
]

#path myapp/quotes/number/2

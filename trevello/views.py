from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):

    dests = Destination.objects.all()
    return render(request, 'index.html', {
        'dests': dests
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def destinations(request):
    return render(request, 'destinations.html')


def elements(request):
    return render(request, 'elements.html')


def news(request):
    return render(request, 'news.html')

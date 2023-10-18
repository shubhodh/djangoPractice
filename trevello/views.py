from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Hyderabad'
    dest1.desc = 'The city of Food'
    dest1.img = '/hyd.jpg'
    dest1.offer = True
    dest1.price = 9000

    dest2 = Destination()
    dest2.name = 'Bengaluru'
    dest2.desc = 'The city of Traffic'
    dest2.img = '/bnglr.jpg'
    dest2.offer = False
    dest2.price = 8000

    dest3 = Destination()
    dest3.name = 'Mumbai'
    dest3.desc = 'The city of Power'
    dest3.offer = True
    dest3.img = '/mum.jpg'
    dest3.price = 8500

    dests = [dest1, dest2, dest3]

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

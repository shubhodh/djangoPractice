from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html', {
        'name': 'Hello Shubhodh welcome'
    })


def add(request):
    n1 = request.GET['num1']
    n2 = request.GET['num2']
    res = int(n1) + int(n2)
    return render(request, 'result.html', {
        'result': res
    })

from random import randrange
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def runr(request):
    context = {
        "title": "Simple example of how to integrate Python With R.",
        "version": "v.0.1",
        "id": randrange(10)
    }
    return render(request, 'index.html', {'context': context})

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    name = "coucou"
    return render(request, 'edulution/home.html', locals())


def subjects(request):
    name = "coucou"
    return render(request, 'edulution/home.html', locals())


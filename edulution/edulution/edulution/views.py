from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Exercise

def login(request):
    name = "coucou"
    return render(request, 'edulution/home.html', locals())


def subjects(request):
    name = "coucou"
    return render(request, 'edulution/home.html', locals())
	
	
def exercise(request):

    path = 'http://198.199.112.173:8008/learn/khan/math/early-math/cc-early-math-place-value-topic/cc-early-math-tens/groups-of-tens/'
    return render(request, 'edulution/exercise.html', locals())


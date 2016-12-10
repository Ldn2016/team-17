from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login


def login(request):
    user = Student(username="edu", user_id="c0041165189a4ac3809b43d0431e9477")
    user.save()
    if request.method == "POST":
        username = request.POST.get('username', '')
        print(username)
        try:
            user = Student.objects.get(username=username)
            print(user)
            request.user = user
            return redirect("/student/subjects/")
        except:
            error = True
            message = "Can't find username, please try 'edu'"
    name = "coucou"
    return render(request, 'edulution/home.html', locals())


def subjects(request):
    return render(request, 'edulution/subjects.html', locals())


def exercise(request):
    name = "coucou"
    return render(request, 'edulution/exercise.html', locals())


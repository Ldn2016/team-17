from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
import json

def login(request):
    user = Student(username="edu", user_id="c0041165189a4ac3809b43d0431e9477")
    user.save()
    if request.method == "POST":
        username = request.POST.get('username', '')
        try:
            user = Student.objects.get(username=username)
            request.session['userid'] = user.user_id
            return redirect("/student/subjects/")
        except Exception as e:
            print(e)
            error = True
            message = "Can't find username, please try 'edu'"
    name = "coucou"
    return render(request, 'edulution/home.html', locals())


def subjects(request):
    try:
        student = Student.objects.get(user_id=request.session['userid'])
    except:
        student = None

    return render(request, 'edulution/subjects.html', locals())


def exercise(request):
    path = 'http://198.199.112.173:8008/learn/khan/math/early-math/cc-early-math-place-value-topic/cc-early-math-tens/groups-of-tens/'
    return render(request, 'edulution/exercise.html', locals())


def test(request, module_id):
    if request.method == "GET":
        the_test = Module.objects.get(id=module_id).associated_test
        questions = Question.objects.filter(test=the_test)
        for i, q in enumerate(questions):
            if q.list_answer:
                questions[i].list_answer = json.loads(q.list_answer)
        for q in questions:
            print(q.list_answer)
        return render(request, 'edulution/test.html', locals())
    elif request.method == "POST":
        pass

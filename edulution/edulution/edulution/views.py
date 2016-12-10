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
    the_test = Module.objects.get(id=module_id).associated_test
    questions = Question.objects.filter(test=the_test)
    if request.method == "GET":
        for i, q in enumerate(questions):
            if q.list_answer:
                questions[i].list_answer = json.loads(q.list_answer)
        questions = [(i, q) for i, q in enumerate(questions)]
        return render(request, 'edulution/test.html', locals())
    elif request.method == "POST":
        student_id = request.session['userid']
        data = request.POST
        correct_answers = []
        answers = []
        for i, q in enumerate(questions):
            correct_answers.append(q.answer)
            answers.append(data.get("answer_question_"+str(i), ''))
        result_in_perc = test_results_to_csv("/tmp/output.csv", answers, correct_answers, student_id, the_test.id)
        return render(request, 'edulution/test.html', locals())


def test_results_to_csv(filename, answers, correctAnswers, studentId, testId):
    assert len(answers) == len(correctAnswers)
    score = 0
    resStr = str(studentId) + ';' + str(testId) + ';'
    for i in range(len(answers)):
        if answers[i] == correctAnswers[i]:
            resStr += '1;'
            score += 1
        else:
            resStr += '0;'

    fo = open(filename, 'w')
    fo.write(resStr + "\n")
    fo.close()
    return (score/len(answers))*100
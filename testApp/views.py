from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def send(request):
    quiz = Quiz.objects.all()
    return render(request, 'testApp/test.html', {'quiz': quiz})


def grade(request):
    quiz = Quiz.objects.all()
    cont = 0
    answer1 = request.POST['1']
    answer2 = request.POST['2']
    answer3 = request.POST['3']
    answer4 = request.POST['4']
    answer5 = request.POST['5']

    if answer1 == 'Option3': cont += 1
    if answer2 == 'Option1': cont += 1
    if answer3 == 'Option3': cont += 1
    if answer4 == 'Option1': cont += 1
    if answer5 == 'Option2': cont += 1

    new_grade = Grade(score=cont)
    new_grade.save()

    return HttpResponse("your score: " + str(cont))

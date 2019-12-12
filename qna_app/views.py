from django.shortcuts import render
from .models import QuestionModel, AnswerModel, CategoryModel

# Create your views here.

def question(requests):
    Question = QuestionModel.objects.all()

    return render(requests, 'questions.html', {'ques':Question})

def popular(request):
    Question = QuestionModel.objects.all()
    return render(request, 'popular.html', {'ques':Question})
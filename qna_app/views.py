from django.shortcuts import render
from .models import QuestionModel, AnswerModel

# Create your views here.

def question(requests):
    Question = QuestionModel.objects.all()

    return render(requests, 'questions.html', {'ques':Question})
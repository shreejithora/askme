from django.shortcuts import render, redirect
from .models import QuestionModel, AnswerModel, CategoryModel
from qna_app.forms import QuestionForm, AnswerForm
from django.http import HttpResponse
from django.views.generic import CreateView, ListView

# Create your views here.

class QuestionListView(ListView):
    queryset = QuestionModel.objects.all()

def question(requests):
    Question = QuestionModel.objects.all()

    return render(requests, 'questionmodel_list.html', {'ques':Question})

def popular(request):
    Question = QuestionModel.objects.all()
    return render(request, 'popular.html', {'ques':Question})

def addquestion(request):
    if(request.method == 'POST'):
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not Valid')
    else:
        # form = QuestionForm
        category = CategoryModel.objects.all()
        return render(request, 'questionmodel_create.html', {'category':category})

def update_question(request, id):
    question = QuestionModel.objects.get(id=id)
    if(request.method == 'POST'):
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not Valid')
    else:
        form = QuestionForm(instance=question)
        return render(request, 'questionmodel_update.html', {'form':form})
    
def del_question(request, id): 
    question = QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:read')

def vote_question(request, id):
    question = QuestionModel.objects.get(id=id)   
    question.question_votes += 1
    question.save()
    return redirect('qna:read')

def add_ans(request, id):
    if request.method == "POST":
        by = request.POST.get('ans_by')
        desc = request.POST.get('ans_desc')
        vote = request.POST.get('ans_votes')
        time = request.POST.get('ans_timestamp')
        img = request.POST.get('ans_img')
        question = QuestionModel.objects.get(id=id)
        comment = AnswerModel(ans_by = by, ans_desc = desc, ans_votes = vote, ans_timestamp = time, ans_img = img, question = question)
        comment.save()
        # return render(request, 'answermodel_create.html', {'answer':answer})
        return HttpResponse('success')
    else:
        form = AnswerForm()
        a = {'form':form}
        b = {'id':id}
        c = {**a, **b}
        return render(request, 'answermodel_create.html', c) 
    
    



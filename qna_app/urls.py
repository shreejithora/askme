"""askmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from qna_app.views import question, popular, addquestion, update_question, del_question, vote_question, add_ans, QuestionListView, add_answer, detail

app_name = 'qna'

urlpatterns = [
    path('view/', question),
    path('popular/', popular),
    path('read/', question,name='read'),
    path('add/', addquestion, name='add'),
    path('update/<int:id>/', update_question,name='update'),
    path('delete/<int:id>/', del_question, name='delete'),
    path('vote/<int:id>/', vote_question, name='vote'),
    path('answeradd/<int:id>/', add_ans, name='addans'),
    path('addanswer/<int:id>/', add_answer, name='comment'), 
    path('listview/', QuestionListView.as_view(), name='listview'),
    path('detail/<int:id>/', detail, name='detail'),


]

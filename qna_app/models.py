from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    cat_title = models.CharField(max_length=120)
    cat_desc = models.TextField(max_length=255)

    def __str__(self):
        return(self.cat_title)


class QuestionModel(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    question_desc = models.TextField()
    question_votes = models.IntegerField(default=0)
    question_img = models.ImageField(upload_to='QuestionImg', blank=True, null=True)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return(self.title)


class AnswerModel(models.Model):
    ans_by = models.CharField(max_length=120)
    ans_desc = models.TextField()
    ans_votes = models.IntegerField(default=0)
    ans_timestamp = models.DateTimeField(auto_now_add=True)
    ans_img = models.ImageField(upload_to="AnswerImg", blank=True, null=True)
    is_accepted = models.BooleanField(default=0)
    question = models.ForeignKey(QuestionModel,on_delete=models.CASCADE)

    def __str__(self):
        return(self.ans_desc[:50]) + '...'






from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') # 추천인 추가
    #  Question 모델에서 사용한 author와 voter가 모두 User 모델과 연결되어 있기 때문에 'User.question_set' 처럼
    #  User 모델을 통해서 Question 데이터에 접근하려고 할 때 author를 기준으로 할지 voter를 기준으로 해야 할지 명확하지 않다
    def __str__(self):
        """
        객체를 문자열로 반환할때 출력되는값
        즉 여기서는 subject가 반환되도록 함
         """
        return self.subject
    def long(self):
        if len(self.content) >= 10:
            return (self.content[:10]+"...")
        else:
            return self.content

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    modify_check = models.BooleanField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')  # 추천인 추가


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_comment') # 추천인 추가
    modify_date = models.DateTimeField(null=True, blank=True)
    modify_check = models.BooleanField(null=True, blank=True)
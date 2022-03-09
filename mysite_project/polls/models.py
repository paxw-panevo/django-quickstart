from datetime import timedelta

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"({self.pk}) {self.question_text}" 
    
    def was_published_recently(self) -> bool:
        the_day_before = timezone.now() - timedelta(days=1)
        return self.pub_date >= the_day_before

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"({self.pk}) {self.choice_text}: {self.votes}" 

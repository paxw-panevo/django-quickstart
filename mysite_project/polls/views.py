from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)

def question_detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def question_results(request, question_id):
    return HttpResponse(f"You're looking at results of question {question_id}.")

def question_vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

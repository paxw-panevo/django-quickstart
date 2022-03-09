from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Question


def index(request):
    latest_questions = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)

def question_detail(request, question_id):
    question = get_object_or_404(
        Question, pk=question_id, pub_date__lte=timezone.now()
    )
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def question_results(request, question_id):
    return HttpResponse(f"You're looking at results of question {question_id}.")

def question_vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

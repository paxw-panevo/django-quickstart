from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)

def question_detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist as exc:
        # Re: `raise ... from` see,
        # https://stackoverflow.com/questions/24752395/python-raise-from-usage
        # https://www.python.org/dev/peps/pep-3134/
        raise Http404('Question does not exist.') from exc
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def question_results(request, question_id):
    return HttpResponse(f"You're looking at results of question {question_id}.")

def question_vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

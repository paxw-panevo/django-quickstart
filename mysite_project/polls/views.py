from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! You're at the polls index.")

def question_detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def question_results(request, question_id):
    return HttpResponse(f"You're looking at results of question {question_id}.")

def question_vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

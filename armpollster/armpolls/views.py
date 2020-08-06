from django.shortcuts import render

# Create your views here.

from .models import Question, choice

# get questions and display them

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'armpolls/index.html', context)

# show specific question and choices

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'armpolls/detail.html', {'question': question})

# Get question and display results

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'armspolls/result.html', {'question': question})

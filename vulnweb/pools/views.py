from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.

def index(request):
    myname = 'Vanh'
    st = ['Phone', 'Plane', 'Computer']
    context = {'name': myname, 'st': st}
    return render(request, "pools/index.html", context)

def view_list(request):
    # list_question = get_object_or_404(Question, pk=3)
    list_question = Question.objects.all()
    context = {'list_quest': list_question}
    return render(request, 'pools/question_list.html', context)

def detail_view(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, 'pools/detail_question.html', {"qs": q})


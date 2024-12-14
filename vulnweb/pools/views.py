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


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST['choice']
        c = q.choice_set.get(pk=data)
    except:
        HttpResponse("Error: Not find choice")
    c.vote += 1
    c.save()
    return HttpResponse(c.vote)


def test_type(request, id):
    return HttpResponse('Test %s' % id)


def test(request):
    latest_question_list = Question.objects.order_by("-time_pub")[:]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


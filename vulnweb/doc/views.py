from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
# Create your views here.

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('doc/index.html')
    context = {
        'lastest_question_list': lastest_question_list,
    }
    # return render(request, 'doc/index.html', context)
    return HttpResponse(template.render(context, request))    



def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Not Found')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'doc/detail.html', {'question':question})




def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
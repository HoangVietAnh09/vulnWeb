from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'doc/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'doc/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = "doc/results.html"


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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "doc/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'doc/detail.html', {'question': question, 'error_message': 'Error'},)
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('doc:results', args=(question.id,)))
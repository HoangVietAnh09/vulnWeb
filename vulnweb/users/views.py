from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import engines
from .models import Users
from .forms import login_form, regist_form

# Create your views here.

def index(request):
    return HttpResponse('Hello users')

def login(request):
    a = login_form()
    return render(request, 'users/login.html', {'f':a})


def ssti(request):
    a = login_form()
    return render(request, 'users/login.html', {'f':a})

def save_info(request):
    if request.method == 'POST':
        r = login_form(request.POST)
        if r.is_valid():
            r.save()
            return HttpResponse('Saved !')
        else:
            return HttpResponse('Unsave')
    else:
        return HttpResponse('Wrong method')
    
def regist_info(request):
    b = regist_form()
    return render(request, 'users/regist.html', {'f': b})

def success(request):
    if request.method == 'POST':
        r = regist_info(request.POST)
        if r.is_valid():
            return HttpResponse('success')
        else:
            return HttpResponse('Somehing wrong')
    else:
        return HttpResponse('Wrong method')

    
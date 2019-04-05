from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello !! Learning using Django with pycharm !!')

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def welcome(request):
    return HttpResponse('Hello World!')


def get_time(request):
    return HttpResponse('Time now is: '+ str(datetime.now()))

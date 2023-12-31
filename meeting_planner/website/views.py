from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

# Create your views here.

def welcome(request):
    return render(request, 'website/welcome.html',
                  {"n_meets": Meeting.objects.count(),
                   "meetings": Meeting.objects.all()})  # multiple vars can be given using commas


def get_time(request):
    return HttpResponse('Time now is: ' + str(datetime.now()))

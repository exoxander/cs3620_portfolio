from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    reply = ""

    return HttpResponse(reply)

def contact(request):
    reply = ""

    return HttpResponse(reply)

def hobbies(request):
    reply = Hobby.objects.all()

    return HttpResponse(reply)

def portfolio(request):
    reply = Portfolio.objects.all()

    return HttpResponse(reply)
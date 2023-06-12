from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    reply = "Welcome to my Portfolio site. I am a CS student at Weber State University in my final semester."

    return HttpResponse(reply)

def contact(request):
    reply = "Contact: Alexanderlustig@mail.weber.edu"

    return HttpResponse(reply)

def hobbies(request):
    reply = Hobby.objects.all()

    return HttpResponse(reply)

def portfolio(request):
    reply = Portfolio.objects.all()

    return HttpResponse(reply)
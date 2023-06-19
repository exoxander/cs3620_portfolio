from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader

# Create your views here.
def home(request):
    
    return render(request, "PortfolioDatabase/home.html")

def contact(request):
    return render(request, "PortfolioDatabase/contact.html")

def hobbies(request):
    item_list = Hobby.objects.all()
    context = {"item_list":item_list,}
    return render(request, "PortfolioDatabase/hobbies.html", context)

def portfolio(request):
    item_list = Portfolio.objects.all()
    context = {"item_list":item_list,}
    return render(request, "PortfolioDatabase/portfolio.html",context)

def hobbyDetails(request, item_id):
    item = Hobby.objects.get(pk=item_id)
    context = {"item":item,}
    return render(request, "PortfolioDatabase/hobbyDetails.html", context)

def portfolioDetails(request, item_id):
    item = Portfolio.objects.get(pk=item_id)
    context = {"item":item,}
    return render(request, "PortfolioDatabase/portfolioDetails.html", context)
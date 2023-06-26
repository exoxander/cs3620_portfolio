from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import editForm
from .forms import messageForm
from .models import *
from django.template import loader
from django.contrib.auth.decorators import login_required

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

@login_required
def upsertItem(request, item_id):

    #if id == 0, in create mode, else in edit mode
    if(item_id != 0):
        try:
            item = Portfolio.objects.get(pk=item_id)
        #if the ID is invalid for some reason, set item to None, then the form goes into create mode
        except:
            item = None
        finally:
            form = editForm(request.POST or None, instance=item)
    else:
        form = editForm(request.POST or None)

    context = {"form":form}
    if(form.is_valid()):
        form.save()
        return redirect("portfolio")

    return render(request, "PortfolioDatabase/portfolio-form.html", context)

@login_required
def deleteItem(request, item_id):
    item = Portfolio.objects.get(pk=item_id)
    context = {"item":item,}

    if(request.method == "POST"):
        item.delete()
        return redirect("portfolio")
    return render(request, "PortfolioDatabase/deleteItem.html", context)

def message(request):
    form = messageForm(request.POST or None)
    context = {"form":form}

    if(form.is_valid()):
        form.save()
        return redirect("contact")

    return render(request, "PortfolioDatabase/contact-form.html", context)

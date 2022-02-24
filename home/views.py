from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'index.html', {})

def feedbacks_view(request, *args, **kwargs):
    return render(request, 'remarks.html', {})

def aboutUs_view(request, *args, **kwargs):
    return render(request, 'aboutUs.html', {})

def joinus_view(request, *args, **kwargs):
    return render(request, 'joinus.html', {})

def buysell_view(request, *args, **kwargs):
    return render(request, 'bucketlist.html', {})

def market_view(request, *args, **kwargs):
    return render(request, 'market.html', {})

def learn_view(request, *args, **kwargs):
    return render(request, 'learn.html', {})

def automobiles_view(request, *args, **kwargs):
    return render(request, 'automobiles.html', {})

def farmers_view(request, *args, **kwargs):
    return render(request, 'workers.html', {})

def products_view(request, *args, **kwargs):
    return render(request, 'products.html', {})





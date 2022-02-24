from django.shortcuts import render, redirect
from products.models import Product
from automobiles.models import Automobile

from django.http import FileResponse
import os


def ministryreport_view(request):
    filepath = os.path.join('static', 'ministry_report.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def allsaleitems_view(request):
    product = Product()
    products = Product.objects.all()

    automobile = Automobile()
    automobiles = Automobile.objects.all()
    context = {
        'products': products,
        'automobiles': automobiles,
    }

    return render(request, 'allsaleitems.html', context)


def learn_view(request):
    return render(request, 'learn.html')


def aboutus_view(request):
    return render(request, 'aboutus.html')


def termsandconditions_view(request):
    return render(request, 'Terms And Conditions.html')

from django.shortcuts import render, redirect
from .forms import AutomobileForm, AppliedAutomobileForm
from .models import Automobile, AppliedAutomobile


# Create your views here.

def automobile_view(request):
    automobile = Automobile()
    automobiles = Automobile.objects.all()

    context = {
        'automobiles': automobiles,

    }

    return render(request, 'automobiles.html', context)


def addautomobile_view(request):
    form = AppliedAutomobileForm()

    if request.method == 'POST':
        form = AppliedAutomobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/automobiles/')

    context = {
        'form': form
    }

    return render(request, 'postautomobile.html', context)

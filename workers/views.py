from django.shortcuts import render, redirect
from .forms import WorkerForm, AppliedWorkerForm
from .models import Worker, AppliedWorker


# Create your views here.

def workers_view(request):
    worker = Worker()
    workers = Worker.objects.all()

    context = {
        'workers': workers,
    }

    return render(request, 'workers.html', context)



def addworker_view(request):
    form = AppliedWorkerForm()

    if request.method == 'POST':
        form = AppliedWorkerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/workers/')

    context = {'form': form}

    return render(request, 'joinform.html', context)



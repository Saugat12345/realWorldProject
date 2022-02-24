from django.shortcuts import render
from .forms import StudentForm, AppliedStudentForm

# Create your views here.
def showform(request):
    form = AppliedStudentForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'studentform.html', context)
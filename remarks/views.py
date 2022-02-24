from django.shortcuts import render, redirect
from .forms import RemarkForm
from .models import Remark


# Create your views here.

def remarkpage_view(request):
    form = RemarkForm()

    if request.method == 'POST':
        form = RemarkForm(request.POST, request.FILES)

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        remarks = request.POST['remarks']

        remark = Remark()
        remark.name = name
        remark.email = email
        remark.message = message
        remark.remarks = remarks

        if form.is_valid():
            remark.save()
            return redirect('#/')


    else:
        return render(request, 'remarks.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView



# Create your views here.

def insiderlogin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect('/insiders/')


    else:
        context = {}

        return render(request, 'insiderlogin.html', context)


def insiderregister_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username,
                                                    password=password1,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
                    user.save()
                    return redirect('/insiders/')
                else:
                    messages.info(request, "Someone already registered with that Email!")
                    return redirect('/insiders/insiderregister/')
            else:
                messages.info(request, "The username is already taken!")
                return redirect('/insiders/insiderregister/')
        else:
            messages.info(request, "Those passwords do not match!")
            return redirect('/insiders/insiderregister/')


    else:
        context = {}

        return render(request, 'insiderregister.html', context)


def loguout_view(request):
    auth.logout(request)
    return redirect('/')




class MyPasswordChangeView(PasswordChangeView):
    template_name = 'editprofile.html'
    success_url = reverse_lazy('users:editprofiledone')

class MyPasswordResetDoneView(PasswordChangeDoneView):
    template_name = 'editprofiledone.html'



def insider_deleteaccount_view(request):
    users = request.user
    user = users.id

    obj = User(id=user)
    obj.delete()
    return redirect('/')

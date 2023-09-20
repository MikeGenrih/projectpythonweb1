from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login
# from .models import authorization
from .forms import RegistrationForm
from .models import UserProfile


def aut(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:

                login(request, user)

                return redirect('book')
            else:
                #### ____>>>>>   <<<<<______
                return redirect('reg')
    else:
        form = LoginForm()
    return render(request, 'authorization/authorization.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            create = UserProfile.objects.create(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )


            return redirect('main')
    else:
        form = LoginForm()

    return render(request, 'authorization/registration.html', {'form': form})

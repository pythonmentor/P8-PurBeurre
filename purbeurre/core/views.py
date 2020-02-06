from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import UserForm

# Create your views here.


def home(request):
    return render(request, 'base.html')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=username, email=email, password=password
                )
            user.save()
        return render(request, 'base.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form': form})

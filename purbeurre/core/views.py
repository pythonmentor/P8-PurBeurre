from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
import logging
# import pdb

from .models import UserRegistrationForm
# Create your views here.

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'base.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=username, email=email, password=password
                )
            user.save()
            user_auth = authenticate(
                request, username=username, password=password
                )
            if user_auth is not None:
                login(request, user_auth)
                logger.error('LOGGED IN!')
                return redirect('home')
            else:
                # error message
                logger.error('Something went wrong!')
                return render(request, 'signup.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')

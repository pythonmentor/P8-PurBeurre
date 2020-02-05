from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.


def home(request):
    return render(request, 'base.html')


def signup(request):
    return render(request, 'signup.html')

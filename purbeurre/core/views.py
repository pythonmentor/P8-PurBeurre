import logging

from core.models import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

# Create your views here.

logger = logging.getLogger(__name__)


class HomePageView(TemplateView):
    template_name = 'base.html'


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('/')
    template_name = 'signup.html'

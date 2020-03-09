from core.models import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.base import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('/')
    template_name = 'signup.html'


class AccountView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = User
    template_name = 'account.html'
    slug_field = 'username'
    slug_url_kwarg = 'user'


class LegalNoticeView(TemplateView):
    template_name = 'legal_notice.html'

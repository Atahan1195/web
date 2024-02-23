from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse


class LoginUserView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return self.request.GET.get('next') or self.request.POST.get('next') or '/'


class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


def logout_user(request):
    logout(request)
    return redirect('home:MainPageView')










from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from . import forms


class RegisterView(CreateView):
    form_class = forms.UserProfileForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse('profile:login')


class AuthorizationView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('book:book_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('profile:login')


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import LoginUserForm, RegisterUserForm


class MyLoginView(LoginView):
    form_class = LoginUserForm
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'


class MyRegisterView(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'




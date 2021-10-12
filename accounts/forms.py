from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, ButtonHolder
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            HTML('<div class="text-center mt-5 b-1">'
                 '<h1 class="h3 mb-3 font-weight-normal">Джуманджи</h1>'
                 '<p class="h5 font-weight-light">Войдите, чтобы управлять</p>'
                 '</div>'),
            'username',
            'password',
            ButtonHolder(Submit('submit', 'Войти', css_class='btn btn-primary btn-lg btn-block')),
            HTML('<div class="mt-4 text-center">'
                 '<p>Нет аккаунта? <a href="{% url "register" %}">Зарегистрируйтесь!</a></p>')
        )


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))

    class Meta:
        model = User

        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            HTML('<div class="text-center mt-5 b-1">'
                 '<h1 class="h3 mb-3 font-weight-normal">Джуманджи</h1>'
                 '<p class="h5 font-weight-light">Создайте аккаунт</p></div>'),
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            ButtonHolder(Submit('submit', 'Зарегистрироваться', css_class='btn btn-primary btn-lg btn-block')),
            HTML('<div class="mt-4 text-center"><p>Есть аккаунт? <a href="{% url "login" %}">Войдите!</a></p></div>')
        )

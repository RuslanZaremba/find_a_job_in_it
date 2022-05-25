from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView

from app_work.forms import SentApplicationForm
from app_work.models import Specialty, Company, Vacancy


class IndexView(TemplateView):
    template_name = 'app_work/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.annotate(total=Count('vacancies'))
        context['companies'] = Company.objects.annotate(total=Count('vacancies'))
        context['title'] = 'Джуманджи'
        return context


class VacanciesListView(ListView):
    model = Vacancy
    template_name = 'app_work/vacancies.html'
    context_object_name = 'vacancies'
    extra_context = {'title': 'Вакансии | Джуманджи', 'name_page': 'Все вакансии'}


class VacanciesByCategoryView(ListView):
    model = Vacancy
    template_name = 'app_work/vacancies.html'
    context_object_name = 'vacancies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialty'] = Specialty.objects.get(code=self.kwargs['specialty'])
        context['title'] = 'Вакансии | Джуманджи'
        return context

    def get_queryset(self):
        return Vacancy.objects.filter(specialty__code=self.kwargs['specialty'])


class CompanyDetailView(ListView):
    model = Vacancy
    template_name = 'app_work/company.html'
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = get_object_or_404(Company, pk=self.kwargs['pk'])
        context['title'] = 'Компания | Джуманджи'
        return context

    def get_queryset(self):
        return Vacancy.objects.filter(company=self.kwargs['pk']).select_related('specialty')


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'app_work/vacancy.html'
    context_object_name = 'vacancy'
    pk_url_kwarg = 'pk'

    def post(self, request, pk):
        form = SentApplicationForm(request.POST)
        user = get_object_or_404(User, id=request.user.id)
        vacancy = get_object_or_404(Vacancy, id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.vacancy = vacancy
            form.user = user
            form.save()
            return redirect(reverse('success_sent_application', args=[pk]))

    def get_context_data(self, *args, **kwargs):
        context = super(VacancyDetailView, self).get_context_data(*args, **kwargs)
        context['form'] = SentApplicationForm()
        return context


class SuccessSentApplication(TemplateView):
    template_name = 'app_work/sent.html'


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена!!!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')

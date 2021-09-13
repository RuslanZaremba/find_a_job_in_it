from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views.generic import TemplateView, ListView, DetailView

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
        context['company'] = Company.objects.get(pk=self.kwargs['pk'])
        context['title'] = 'Компания | Джуманджи'
        return context

    def get_queryset(self):
        return Vacancy.objects.filter(company=self.kwargs['pk'])


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'app_work/vacancy.html'
    context_object_name = 'vacancy'
    pk_url_kwarg = 'pk'


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена!!!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')

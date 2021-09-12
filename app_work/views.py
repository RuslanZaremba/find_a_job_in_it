from django.db.models import Count
from django.views.generic import TemplateView, ListView, DetailView

from app_work.models import Specialty, Company, Vacancy


class IndexView(TemplateView):
    template_name = 'app_work/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.annotate(total=Count('vacancies'))
        context['companies'] = Company.objects.annotate(total=Count('vacancies'))
        return context


class VacanciesList(ListView):
    model = Vacancy
    template_name = 'app_work/vacancies.html'
    context_object_name = 'vacancies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.annotate(total=Count('vacancies'))
        return context


class VacanciesByCategory(ListView):
    model = Vacancy
    template_name = 'app_work/vacancies.html'
    context_object_name = 'vacancies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialty'] = Specialty.objects.get(code=self.kwargs['specialty'])
        context['total_vacancies'] = Vacancy.objects.filter(specialty__code=self.kwargs['specialty']).count()
        return context

    def get_queryset(self):
        return Vacancy.objects.filter(specialty__code=self.kwargs['specialty'])


# class CompanyDetail(DetailView):
#     model = Company
#     template_name = 'app_work/company.html'
#     context_object_name = 'company'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         vacancies_for_company_detail = Vacancy.objects.filter(company=kwargs["object"].pk)
#         total_vacancies = vacancies_for_company_detail.count()
#
#         context['vacancies'] = vacancies_for_company_detail
#         context['total_vacancies'] = total_vacancies
#
#         return context

class CompanyDetail(ListView):
    model = Vacancy
    template_name = 'app_work/company.html'
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.get(pk=self.kwargs['pk'])
        context['total_vacancies'] = Vacancy.objects.filter(company=self.kwargs['pk']).count()
        return context

    def get_queryset(self):
        return Vacancy.objects.filter(company=self.kwargs['pk'])


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'app_work/vacancy.html'
    context_object_name = 'vacancy'
    pk_url_kwarg = 'pk'
